#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

import numpy as np
from functools import partial
from collections import defaultdict, deque

"""
https://stackoverflow.com/questions/25014298/creating-a-defaultdict-with-empty-numpy-array/25014320
"""


class LevelSort:

    def __init__(self):
        self._link = np.array(range(10))
        self._data = defaultdict(partial(np.array, False))
        self._cops = None
        self._linked = deque() # FIFO

    def _gen_key(self, item):
        return f"{len(item)}:{0 if len(item) == 1 else item[:-1]}"

    def _gen_value(self, item):
        return np.array(item, dtype=np.int64) if len(item) == 1 else np.array(item[-1], dtype=np.int64)

    def load(self):
        if self._linked:
            for _ in range(len(self._linked)):
                self._data[self._linked.pop()] = self._link

    def _load_copy(self, key):
        if self._cops and key in self._cops:
            del self._cops[self._cops.index(key)]
            return self._link
        else:
            return self._data[key]

    def dump(self):
        for key in self._data.keys():
            item = self._data[key]
            if len(item) == 10 and not set(self._link) ^ set(item):
                self._data[key] = np.array(['a'])
                self._linked.append(key)

    def add(self, iterable):
        if isinstance(iterable, (str, bool, float)):
            assert isinstance(iterable, int), 'Need integer, or list of integers'

        if isinstance(iterable, int):
            iterable = [iterable]

        for item in iterable:
            item = str(item)
            ftem = self._gen_key(item)
            if self._data[ftem].dtype != np.bool:
                self._data[ftem] = np.append(
                    self._link if self._data[ftem].dtype != np.int64 else self._data[ftem],
                    self._gen_value(item)
                )
            else:
                self._data[ftem] = self._gen_value(item)

    def get(self):
        self._cops = self._linked.copy()
        return (values for key in sorted(self._data.keys())
                       for values in self._load_copy(key)
                                    + (int(f"{key.split(':')[1]}0")))

    def clear(self):
        self._data.clear()
        self._linked.clear()
