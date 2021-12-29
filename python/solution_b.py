"""
Assignment
==============
- Problem Statement:
      Write a program to count the number of possible outcomes of 10 tosses
      of a coin where the output has no consecutive three tails

Professor: Dr. Abdallah
Department: Computers And Systems Engineering
Solution B: dynamic programming
"""


from typing import Dict


# using top-down approach
def coin_possibilities_tda(tosses: int, not_allowed: int, memo: Dict[int, int] = None) -> int:
    """coin_possibilities_tda(tosses, not_allowed, memo)

    Count the number of possibilities (sequences of heads and tails) resulting from tossing a coin.
    tosses:       the number of tosses that will be considered
    not_allowed:  the number of tails that are not allowed to be consecutive
    memo:         a hashtable (dictionary) that will be used to store the results of different tosses to use them later (instead of recalculating them)

    this function uses top-down approach to solve the problem"""

    if memo is None:
        memo = {}

    if tosses == -1 or tosses == 0:
        return 1

    if tosses < not_allowed:
        if memo.get(tosses - 1) is None:
            memo[tosses - 1] = coin_possibilities_tda(tosses - 1, not_allowed, memo)
        return memo[tosses - 1] * 2

    if memo.get(tosses - 1) is None:
        memo[tosses - 1] = coin_possibilities_tda(tosses - 1, not_allowed, memo)

    if memo.get(tosses - 1 - not_allowed) is None:
        memo[tosses - not_allowed - 1] = coin_possibilities_tda(tosses - not_allowed - 1, not_allowed, memo)

    return memo[tosses - 1] * 2 - memo[tosses - not_allowed - 1]


# using buttom-up approach
def coin_possibilities_bua(tosses: int, not_allowed: int) -> int:
    """coin_possibilities_bua(tosses, not_allowed)

    Count the number of possibilities (sequences of heads and tails) resulting from tossing a coin.
    tosses:       the number of tosses that will be considered
    not_allowed:  the number of tails that are not allowed to be consecutive

    this function uses buttom-up approach to solve the problem"""

    dp_list = [0] * (tosses + 2)
    dp_list[0] = 1
    dp_list[1] = 1

    for i in range(2, tosses + 2):
        if i - 1 < not_allowed:
            dp_list[i] = dp_list[i - 1] * 2
        else:
            dp_list[i] = dp_list[i - 1] * 2 - dp_list[i - not_allowed - 1]

    return dp_list[tosses + 1]


if __name__ == "__main__":
    tosses = int(input("number of tosses: "))
    not_allowed = int(input("number of tails not allowed to be consecutive: "))
    print(f"tda: tosses = {tosses} , not_allowed = {not_allowed} => {coin_possibilities_tda(tosses, not_allowed)}")
    print(f"bua: tosses = {tosses} , not_allowed = {not_allowed} => {coin_possibilities_bua(tosses, not_allowed)}")
