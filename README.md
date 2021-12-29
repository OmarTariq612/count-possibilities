# Counting Outcomes
## Problem Statement

    Write a program to count the number of possible outcomes of 10 tosses
    of a coin where the output has no consecutive three tails
## Solution A

This solution uses a user-defined function (predicate) to determine whether this outcome should be considered valid or not.

### pros
This solution is general and can be applied to other problems not just (tossing the coin problem) as the user provides the possible options (2 in the coin problem) and the predicate.

### cons
Time Complexity: O(number_of_options ^ required_length)
## Solution B

This solution uses dynamic programming to solve the problem.

### pros
Time Complexity: O(required_length)

### cons
This solution is limited to (tossing the coin problem).
