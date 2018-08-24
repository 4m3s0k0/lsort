#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from make_dict import _dict
from collections import defaultdict


def _levels():
    """
    # INPUT
    defaultdict(
        <class 'list'>, {
            '1': [1, 5, 0],
            '2': [12, 78, 25],
            '3': [548, 713]
        }
    )

    # OUTPUT
    defaultdict(
        <class 'dict'>, {
            '1': {
                '0': [1, 5, 0]  # '0' + str([@]) -> int('0@')
            },
            '2': {
                '1': [2],   # '1' + str([1]) -> int('12')
                '7': [8],   # '7' + str([7]) -> int('78')
                '2': [5],   # '2' + str([2]) -> int('25')
            },
            '3': {
                '54': [8],  # '54' + str([8]) -> int('548')
                '71': [3],  # '71' + str([3]) -> int('713')
            }
        }
    )

    # WHAT I NEED: defaultdict(list) inside dict
    >>> levels['1']['0']
    >>> []

    # HOW I CAN REALIZE IT: ...
    >>> levels = defaultdict({}, defaultdict(list)) | NAH HELP
    >>> levels = defaultdict(dict)
    >>> levels['1']['0'].append(1)  | ERROR, but OUTPUT ... {'1': {}}
    >>> levels['1']['0']            | ERROR, but OUTPUT ... {'1': {}}
    >>> levels['1']['0'] = []
    >>> defaultdict(<class 'dict'>, {'1': {'0': []}})

    ---------------------------------
    try:
        levels['key']['0'].append(1)
    except KeyError:
        levels['key']['0'] = [1]
    ---------------------------------

    >>> _levels(_dict([1, 12, 78, 25, 5, 0, 548, 713]))
    defaultdict(<class 'dict'>, {'1': {'0': [1, 5, 0]}, ... '3': {'54': [8], '71': [3]}})

    """
    _dt = _dict([1, 12, 78, 25, 5, 0, 548, 713])
    levels = defaultdict(dict)

    for key in _dt.keys():
        for item in _dt[key]:
            item = str(item)
            try:
                # level = '0' if len(item) == 1 else item[:-1]
                # {'0': [0 ... 9]}
                levels[key][
                    '0' if len(item) == 1 else item[:-1]
                ].append(int(item) if len(item) == 1 else int(item[-1]))
                #
            except KeyError:
                # items = item if len(item) == 1 else item[:-1])
                # if item == level['0'] then item = item, else item[:-1]
                # '0' -> '0', '10' -> '1'
                levels[key][
                    '0' if len(item) == 1 else item[:-1]
                ] = [int(item) if len(item) == 1 else int(item[-1])]

    return levels


if __name__ == "__main__":
    print(_levels(_dict([1, 12, 78, 25, 5, 0, 548, 713])))
