#!/usr/bin/python3
"""
This script solves this question:
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """ This function finds fewest number of coins needed to meet
    a given amount total. """
    coins_sum = sum(coins)
    if total <= 0:
        return 0

    if coins_sum > total:
        return -1
    elif coins_sum < total:
        return total - coins_sum
