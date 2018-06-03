"""Coins.

Given an infinite supply of quarters dimes, nickels, and pennies,
wrote code to represent the number of ways to represent n cents.
"""


def calc_num_coins(n):
    """Calc the num of coins."""
    def add_coin(total=0):
        """."""
        if total > n:
            return 0
        if total == n:
            return 1

        return add_coin(total + 1) + add_coin(total + 5) + add_coin(total + 10) + add_coin(total + 25)

    return add_coin()
