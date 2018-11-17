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
        self._linked = deque() # FIFO

    def _gen_key(self, item):
        return f"{len(item)}:{0 if len(item) == 1 else item[:-1]}"

    def _gen_value(self, item):
        return np.array(item, dtype=np.int64) if len(item) == 1 else np.array(item[-1], dtype=np.int64)

    def _load(self):
        for _ in range(len(self._linked)):
            self._data[self._linked.pop()] = self._link

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

        # it shouldn't change data
        if self._linked:
            self._load()

        return (values for key in sorted(self._data.keys())
                       for values in self._data[key]
                                    + (int(f"{key.split(':')[1]}0")))

    def clear(self):
        self._data.clear()


if __name__ == "__main__":
    ls = LevelSort()
    t1 = [1, 5, 9]
    print('adding:', t1)
    ls.add(t1)
    print('data:', ls._data)
    t2 = range(10, 45)
    print('adding:', t2)
    ls.add(t2)
    print('data:', ls._data)
    print('dumping...')
    ls.dump()
    print('data:', ls._data)
