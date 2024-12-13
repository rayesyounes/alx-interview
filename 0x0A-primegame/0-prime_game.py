#!/usr/bin/python3
"""
docs
"""


def primes(n):
    """
    docs
    """
    prime_numbers = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime_numbers.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime_numbers


def isWinner(num_rounds, nums):
    """
    docs
    """
    if not num_rounds or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(num_rounds):
        prime_numbers = primes(nums[i])
        if len(prime_numbers) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None