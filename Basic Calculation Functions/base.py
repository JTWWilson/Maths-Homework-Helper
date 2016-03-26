import math


def add(*nums):
    """
    Return all of the arguments added together
    :argument nums: All of the given arguments
    :returns sum(nums): The total of all of the arguments
    """
    return sum(nums)


def take(x, y):
    """
    Take two numbers away from each other
    :argument x: Take y away from this
    :argument y: Take this from x
    :returns x-y: x take y
    """
    return x-y


def times(*nums):
    """
    Multiply all arguments together
    :argument nums: All the arguments given
    :returns total: The result of multiplying them all together
    """
    total = 1
    for i in nums:
        total *= i
    return total


def divide(x, y):
    """
    Returns x divided by y
    :argument x: Gets divided by y
    :argument y: Divide x by this
    :returns x/y: x divided by y
    """
    return x/y


def power(x, y=2):
    """
    Returns x to the power of y
    :argument x: Number indexed
    :argument y: Index x is taken to (defaults to two)
    :returns x**y: X to the power of y
    """
    return x**y


def simplify(clause):
    """
    Returns a simplified version of an equation
    :argument clause: Clause taken in to be simplified
    """
