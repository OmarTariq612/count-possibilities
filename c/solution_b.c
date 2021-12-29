/**
 * @file solution_b.c
 * @author Omar Tariq Abdel-Raziq
 * @brief - Problem Statement:
 *              Write a program to count the number of possible outcomes of 10 tosses
 *              of a coin where the output has no consecutive three tails
 *
 * Solution B: dynamic programming 
 * @copyright Copyright (c) 2021
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/**
 * @brief counts the number of possibilities (sequences of heads and tails) resulting from tossing a coin.
 * 
 * @param tosses the number of required tosses
 * @param not_allowed the number of tails that are not allowed to be consecutive.
 * @return size_t
 */
size_t coin_possibilities(int tosses, int not_allowed);

int main(int argc, char *argv[])
{
    int tosses, not_allowed;
    printf("number of tosses: ");
    scanf("%d", &tosses);

    printf("number of tails not allowed to be consecutive: ");
    scanf("%d", &not_allowed);

    printf("%lu\n", coin_possibilities(tosses, not_allowed));

    return 0;
}

size_t coin_possibilities(int tosses, int not_allowed)
{
    assert(tosses > 0);
    assert(not_allowed > 0);

    size_t *dp_list = malloc(sizeof(size_t) * (tosses + 2));
    assert(dp_list != NULL);
    dp_list[0] = 1;
    dp_list[1] = 1;

    for (int i = 2; i < tosses + 2; i++)
    {
        if (i - 1 < not_allowed)
            dp_list[i] = dp_list[i - 1] * 2;
        else
            dp_list[i] = dp_list[i - 1] * 2 - dp_list[i - not_allowed - 1];
    }

    size_t result = dp_list[tosses + 1];
    free(dp_list);
    return result;
}