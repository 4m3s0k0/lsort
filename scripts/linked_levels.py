#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from make_levels import _levels


def _linked():
    """
    #                 INPUT     | # OUTPUT
    defaultdict(                |
        <class 'dict'>, {       |
            '1': {              |
                '0': [1, 5, 0]  | ['F', 0, 1, 5]
            },                  |
            '2': {              |
                '1': [2],       | ['F', 2]
                '7': [8],       | ['F', 8]
                '2': [5],       | ['F', 5]
            },                  |
            '3': {              |
                '54': [8],      | ['F', 8]
                '71': [3],      | ['F', 3]
            }                   |
        }                       |
    )                           |

    ---------------------------------
    >>> link = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> targ = [0, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> set(link) ^ set(targ)
    {1}
    >>> targ = ['F'] + targ
    ['F', 0, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> ntrg = list(range(10))
    >>> set(link) ^ set(ntrg)
    {}
    ---------------------------------

    """
    link = list(range(10))
    levels = _levels()

    # F -> FALSE, NOT LINKED LIST
    F = True
    # '1' -> len(n)
    for keys in levels:
        # '0' -> level(n)
        for key in levels[keys]:
            # level items -> [0 ... 9]
            item = levels[keys][key]
            if len(item) == len(link):
                if not set(link) ^ set(item):
                    # 'T' -> True, use link
                    # link already sorted
                    levels[keys][key] = ['T']
                    F = False
            if F:
                item.sort()
                levels[keys][key] = ['F'] + item

    return levels


if __name__ == "__main__":
    print(_linked())
