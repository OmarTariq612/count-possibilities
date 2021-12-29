/**
 * @file solution_a.c
 * @author Omar Tariq Abdel-Raziq
 * @brief - Problem Statement:
 *              Write a program to count the number of possible outcomes of 10 tosses
 *              of a coin where the output has no consecutive three tails
 *
 * Solution A: user-defined function (predicate) 
 * @copyright Copyright (c) 2021
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <stdbool.h>
#include <assert.h>

/**
 * @brief a user-defined function to eleminate outcomes that have 3 consecutive tails.
 * 
 * @param sequence is the sequence that will be checked.
 * @param length is the length of that sequence.
 */
bool predicate(const char *sequence, size_t length);

/**
 * @brief an interface to the recursive function (count_possibilities_rec).
 * 
 * @param length is the required length of each possibility.
 * @param sequence is the sequence that contains the options from which we can choose.
 * @param is_valid is a function that takes a sequence before considering it while counting to determine if this sequence should be treated as a valid one or not.
 * @return size_t 
 */
size_t count_possibilities(int length, const char *sequence, bool (*is_valid)(const char *, size_t));

/**
 * @brief Count the number of possibilities of length "length" that can be generated from the "sequence".
 * 
 * @param length is the required length of each possibility.
 * @param sequence is the sequence that contains the options from which we can choose.
 * @param is_valid is a function that takes a sequence before appending an item to it to determine if this sequence should be treated as a valid one or not
 * @param res_string 
 * @param res_string_length 
 * @return size_t 
 */
size_t count_possibilities_rec(int length, const char *sequence, bool (*is_valid)(const char *, size_t), char *res_string, size_t res_string_length);

int main(int argc, char *argv[])
{
    int tosses;
    printf("number of tosses: ");
    scanf("%d", &tosses);

    printf("count = %lu\n", count_possibilities(tosses, "HT", predicate));

    return 0;
}

bool predicate(const char *sequence, size_t length)
{
    if (length < 3)
        return true;

    return strncmp(sequence + length - 3, "TTT", 3) != 0;
}

size_t count_possibilities(int length, const char *sequence, bool (*is_valid)(const char *, size_t))
{
    assert(length > 0);
    assert(sequence != NULL);
    assert(is_valid != NULL);
    char *buffer = calloc(length + 1, sizeof(char)); // the last char is for "string termination"
    assert(buffer != NULL);
    size_t count = count_possibilities_rec(length, sequence, is_valid, buffer, 0);
    free(buffer);
    return count;
}

size_t count_possibilities_rec(int length, const char *sequence, bool (*is_valid)(const char *, size_t), char *res_string, size_t res_string_length)
{
    if (res_string_length == length)
        return 1;

    size_t possibilities_count = 0;

    for (int i = 0, n = strlen(sequence); i < n; i++)
    {
        res_string[res_string_length] = sequence[i];

        if (is_valid(res_string, res_string_length + 1))
            possibilities_count += count_possibilities_rec(length, sequence, is_valid, res_string, res_string_length + 1);
    }

    return possibilities_count;
}