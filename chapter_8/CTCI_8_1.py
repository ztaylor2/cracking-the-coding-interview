"""Triple Step.

A child is running up a staircase with n steps and can hop either 1 step,
2 steps, or 3 steps. How many possible ways can the child step to get to
the top of the staircase?
"""


def num_steps(n, steps=0):
    """Determine number of ways a child can get to the top of the stairs."""
    if steps > n:
        return 0
    if steps == n:
        return 1
    return num_steps(n, steps + 1) + num_steps(n, steps + 2) + num_steps(n, steps + 3)
