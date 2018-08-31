#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from collections import defaultdict


class LevelSort:
    """
    Container like, ten (10) with nteen:
        add 10 (n==10) to key '2:1' with logic if len(n)==2 and n.startswith('1')

    >>> ls = LevelSort()
    >>> t1 = [1, 5, 9]
    >>> ls._add(t1)
    >>> ls._llevels
    defaultdict(list, {'1:0': [1, 5, 9]})
    >>> ls._get()
    [1, 5, 9]
    >>>
    >>> t2 = [16, 17, 11, 25, 20, 29, 78, 89]
    >>> ls._add(t2)
    >>> ls._llevels
    defaultdict(<class 'list'>, {
        '1:0': [1, 5, 9],
        '2:1': [6, 7, 1],
        '2:2': [5, 0, 9],
        '2:7': [8],
        '2:8': [9]
        }
    )
    >>>
    >>> ls._get()
    [1, 5, 9, 16, 17, 11, 25, 20, 29, 78, 89]
    >>> ls._new()
    >>> ls._llevels
    defaultdict(<class 'list'>, {})
    """

    def __init__(self):
        self._link = list(range(10))
        self._llevels = defaultdict(list)

    def __len__(self):
        """
        Return length of keys in *_llevels*
        """
        return len(self._llevels.keys())

    def __repr__(self):
        """
        Print in instance call
        """
        return 'ins of <class LevelSort>'

    def __linked_levels(self):
        """
        All levels have numbers f0 ... t9
        I will remove repeating numbers with adding 'T'
        'T' -> True,  i already have numbers in *self._link*
        Exp: [0, 9, 8, 5, 2, 3, 7, 6, 1, 4] > ['T']
        """
        for key in self._llevels:
            item = self._llevels[key]
            if 10 == len(item):
                if not set(self._link) ^ set(item):
                    self._llevels[key] = ['T']

    def __ftem(self, item):
        """
        Return Key for *_llevels*
        """
        return "{}:{}".format(
            len(item), '0' if len(item) == 1 else item[:-1]
        )

    def __levels(self, _input):
        """
        _llevels['2:1'] > 2: len(item in _input), 1: 1st level < [15][:-1]
        """
        for item in _input:
            item = str(item)
            self._llevels[self.__ftem(item)].append(
                int(item) if len(item) == 1 else int(item[-1])
            )
        self.__linked_levels()

    def _add(self, _input):
        """
        :arg:   _input: integer or list of integers
        ---------------------------------
        1st _add: creates linked list
        2nd _add: appends to the linked list
        """
        # LS SORTING ONLY INTEGERS
        if isinstance(_input, (str, bool, float)):
            assert isinstance(_input, int), 'Need integer, or list of integers'
        # INT TO LIST
        if isinstance(_input, int):
            _input = [_input]
        # 1st AND 2nd CALL
        if not self._llevels:
            # CREATE LINKED LIST
            self.__levels(_input)
        else:
            # APPEND TO LINKED LIST
            for item in _input:
                item = str(item)
                ftem = self.__ftem(item)
                if ftem in self._llevels.keys():
                    if self._llevels[ftem][0] == 'T':
                        self._llevels[ftem] = self._link
                        self._llevels[ftem].append(
                            int(item) if len(item) == 1 else int(item[-1])
                        )
                    else:
                        self._llevels[ftem].append(int(item[-1]))
                else:
                    self._llevels[ftem] = [int(item[-1])]
            self.__linked_levels()

    def _get(self):
        """
        Return list of numbers
        """
        glvl = []
        skey = list(self._llevels.keys())
        skey.sort()
        for gkey in skey:
            lkey = gkey.split(':')[1]   # len(n):level(n)
            if self._llevels[gkey][0] == 'T':
                glvl.extend(
                    [int('{}{}'.format(lkey, each)) for each in self._link]
                )
            else:
                glvl.extend(
                    [int('{}{}'.format(lkey, each)) for each in self._llevels[gkey]]
                )
        return glvl

    def _new(self):
        """
        Clear *_llevels*
        """
        self._llevels.clear()


if __name__ == "__main__":
    ls = LevelSort()
    print(ls.__doc__)
