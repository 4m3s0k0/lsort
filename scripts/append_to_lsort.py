#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from linked_levels import _linked


def _append(llike):
    """
    # INPUT [1, 11, 22, 333, 4444, 55555, 666666]
    ---------------------------------

    #                  LEVELS           | # OUTPUT
    defaultdict(                        |
        <class 'dict'>, {               |
            '1': {                      |
                '0': ['F', 1, 5, 0]     | '0':      ['F', 0, 1, 1, 5]
            },                          |
            '2': {                      |
                '1': ['F', 2],          | '1':      ['F', 1, 2]
                '7': ['F', 8],          | '7':      ['F', 8]
                '2': ['F', 5],          | '2':      ['F', 2, 5]
            },                          |
            '3': {                      |
                '54': ['F', 8],         | '54':     ['F', 8]
                '71': ['F', 3],         | '71':     ['F', 3]
            }                           | '33':     ['F', 3]
        }                               |
    )                                   | '444':    ['F', 4]
    #                                   | '5555':   ['F', 5]
    #                                   | '66666':  ['F', 6]

    """
    link = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_levels = _linked()

    if isinstance(llike, (str, bool)):
        assert isinstance(llike, int), 'Need integer, or list of integers'

    if isinstance(llike, int):
        llike = [llike]

    # print(linked_levels)
    for item in llike:
        item = str(item)
        meti = '0' if len(item) == 1 else item[:-1]
        leni = str(len(item))
        if meti in linked_levels[leni].keys():
            if linked_levels[leni][meti][0] == 'T':
                newi = link + [int(item) if len(item) == 1 else int(item[-1])]
                newi.sort()
                linked_levels[leni][meti] = newi
            else:
                newi = [int(item[-1])] + linked_levels[leni][meti][1:]
                newi.sort()
                linked_levels[leni][meti][1:] = newi
        else:
            linked_levels[leni][meti] = ['F', int(item[-1])]

    return linked_levels


if __name__ == "__main__":
    print(_append([1, 11, 22, 333, 4444, 55555, 666666]))
