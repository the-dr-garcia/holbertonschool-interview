#!/usr/bin/python3
"""
Module for the making change problem
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): values of the coins available (infinite supply)
        total (int): target amount

    Returns:
        int: fewest number of coins needed to meet total,
             0 if total <= 0, -1 if total cannot be met
    """
    if total <= 0:
        return 0

    coins = [c for c in set(coins) if 0 < c <= total]
    if not coins:
        return -1

    inf = total + 1
    dp = [0] + [inf] * total

    for coin in coins:
        for amount in range(coin, total + 1):
            candidate = dp[amount - coin] + 1
            if candidate < dp[amount]:
                dp[amount] = candidate

    return dp[total] if dp[total] != inf else -1
