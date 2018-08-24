#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from collections import defaultdict


def _dict(nums):
    """
    # INPUT
    [1, 12, 78, 25, 5, 0, 548, 713]

    # OUTPUT
    defaultdict(
        <class 'list'>, {
            '1': [1, 5, 0],
            '2': [12, 78, 25],
            '3': [548, 713]
        }
    )

    ---------------------------------
    >>> dct = defaultdict(list)
    >>> dct['1']
    []
    >>> dct['1'].append(6)
    >>> dct['1']
    [6]

    ---------------------------------
    # WITHOUT defaultdict
    try:
        dct['1']
    except KeyError:
        dct['1'] = [6]
    ---------------------------------

    >>> _dict([1, 12, 78, 25, 5, 0, 548, 713])
    defaultdict(<class 'list'>, {'1': [1, 5, 0], '2': [12, 78, 25], '3': [548, 713]})

    """
    dct = defaultdict(list)

    for n in nums:
        dct["{}".format(len(str(n)))].append(n)

    return dct


if __name__ == "__main__":
    print(_dict([1, 12, 78, 25, 5, 0, 548, 713]))
