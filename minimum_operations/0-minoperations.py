#!/usr/bin/python3
"""
Module that calculates the fewest number of operations needed
to result in exactly n H characters in a text file, using only
'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations (Copy All + Paste)
    needed to reach exactly n 'H' characters, starting from 1 'H'.

    The approach relies on prime factorization: each prime factor
    of n represents a 'Copy All' followed by (factor - 1) 'Paste'
    operations, so the total number of operations for that factor
    is the factor itself. Summing the prime factors (with
    repetition) gives the minimum total number of operations.

    This method avoids building any array or history of states
    (no dynamic programming table), keeping memory usage O(1)
    regardless of the size of n.

    Args:
        n (int): the target number of 'H' characters.

    Returns:
        int: the fewest number of operations needed to reach
            exactly n characters, or 0 if n is impossible to
            achieve (n < 2).
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
