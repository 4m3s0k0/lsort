#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from pickle import dump #-----------#
from collections import defaultdict #
from append_to_lsort import _append #


def _gdict(logit=False):
    """
    # OUTPUT
    defaultdict(
        <class 'list'>, {
            '1': [0, 1, 1, 5],
            '2': [11, 12, 22, 25, 78],
            '3': [333, 548, 713],
            '4': [4444],
            '5': [55555],
            '6': [666666]
        }
    )

    # POSITION
    defaultdict(
        <class 'dict'>, {
            '1': {
                '0': (0, 4)
            },
            '2': {
                '1': (0, 2),
                '2': (2, 4),
                '7': (4, 5)
            },
            '3': {
                '33': (0, 1),
                '54': (1, 2),
                '71': (2, 3)
            },
            '4': {
                '444': (0, 1)
            },
            '5': {
                '5555': (0, 1)
            },
            '6': {
                '66666': (0, 1)
            }
        }
    )

    ---------------------------------
    >>> m = list(range(10))
    >>> (m.index(m[0]), len(m))
    (0, 10)
    ---------------------------------

    """
    dct = _append([1, 11, 22, 333, 4444, 55555, 666666])
    gtd = defaultdict(list)
    if logit:
        log = defaultdict(dict)
        ffp = 'position.pickle'
    link = list(range(10))
    _key = []
    _keys = []

    for keys in dct.keys():
        _keys.append(int(keys))
        _key.append([int(each) for each in dct[keys].keys()])

    key_keys = dict(zip(_keys, _key))
    position = 0
    _keys.sort()
    del _key

    for gkeys in _keys:
        key_keys[gkeys].sort()
        for lengk in key_keys[gkeys]:
            # LENGTH
            gkeys = str(gkeys)
            # LEVEL
            lengk = str(lengk)
            pposi = 0 if position == 0 else position
            if dct[gkeys][lengk][0] == 'T':
                gtd[gkeys].extend(
                    [int('{}{}'.format(lengk, each)) for each in [link]]
                )
                if logit:
                    log[gkeys][lengk] = (pposi, pposi + 10)
                    position = pposi + 10
            else:
                gtd[gkeys].extend(
                    [int('{}{}'.format(lengk, each)) for each in dct[gkeys][lengk][1:]]
                )
                if logit:
                    position += len(dct[gkeys][lengk][1:])
                    log[gkeys][lengk] = (pposi, position)
        position = 0

    del _keys
    del key_keys

    if logit:
        with open(ffp, 'wb') as file_for_position:
            dump(log, file_for_position)
        del log
    return gtd


if __name__ == "__main__":
    print(_gdict(True))
