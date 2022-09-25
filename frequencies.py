"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    str_items = [str(i) for i in items]
    for i in str_items:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies
