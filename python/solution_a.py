"""
Assignment
==============
- Problem Statement:
      Write a program to count the number of possible outcomes of 10 tosses
      of a coin where the output has no consecutive three tails

Professor: Dr. Abdallah
Department: Computers And Systems Engineering
Solution A: user-defined function (predicate)
"""


from typing import Generator, Sequence, Tuple, Callable, Union


def count_possibilities(
    length: int,
    sequence: Union[str, Sequence[str]],
    is_valid: Callable[[Tuple[str]], bool],
    res_tuple: Tuple[str] = tuple()
) -> int:
    """Count the number of possibilities of length 'length' that can be generated from the 'sequence'
    
    count_possibilities(length, sequence, pred, res_tuple)
    length: the required length of each possibility
    sequence: the sequence that contains the options from which we can choose
    is_valid: a function that takes a sequence before appending an item to it to determine if this sequence should be treated as a valid one or not"""

    if len(res_tuple) == length:
        return 1

    possibilities_count = 0

    for item in sequence:
        if is_valid(res_tuple + (item,)):
            possibilities_count += count_possibilities(length, sequence, is_valid, res_tuple + (item,))

    return possibilities_count

def possibilities_generator(
    length: int,
    sequence: Union[str, Sequence[str]],
    is_valid: Callable[[Tuple[str]], bool] = None,
    res_tuple: Tuple[str] = tuple()
) -> Generator[Tuple[str], None, None]:
    """Generate the possibilities of length 'length' that can be generated from the 'sequence' using generators

    possibilities_generator(length, sequence, pred, res_tuple)
    length: the required length of each possibility
    sequence: the sequence that contains the options from which we can choose
    is_valid: a function that takes a sequence before considering it while counting to determine if this sequence should be treated as a valid one or not"""

    if len(res_tuple) == length:
        yield res_tuple
        return

    if is_valid:
        for item in sequence:
            if is_valid(res_tuple + (item,)):
                yield from possibilities_generator(length, sequence, is_valid, res_tuple + (item,))
    else:
        for item in sequence:
            yield from possibilities_generator(length, sequence, is_valid, res_tuple + (item,))


def predicate(seq: Tuple[str]) -> bool:
    if len(seq) < 3:
        return True
    
    return "".join(seq[-3:]) != "TTT"

if __name__ == "__main__":
    number = int(input("number of tosses: "))
    print(f"count = {count_possibilities(number, 'HT', predicate)}")

    # you can uncomment the following snippet to print the possibilities themselves
    # for possibility in possibilities_generator(number, "HT", predicate):
    #     print(possibility)