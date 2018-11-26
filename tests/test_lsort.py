#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from sys import path
path.insert(0, '..')

from lsort.lsort import LevelSort


"""
adding: [0, 1, 2, 3]

data: defaultdict(..., {'1:0': array([0, 1, 2, 3])})

adding: range(4, 15)
data: defaultdict(..., {'1:0': array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), '2:1': array([0, 1, 2, 3, 4])})

dumping...
data: defaultdict(..., {'1:0': array(['a'], dtype='<U1'), '2:1': array([0, 1, 2, 3, 4])})
"""


if __name__ == "__main__":
    ls = LevelSort()
    t1 = [0, 1, 2, 3]
    print('adding:', t1)
    ls.add(t1)
    print('\ndata:', ls._data)
    t2 = range(4, 15)
    print('\nadding:', t2)
    ls.add(t2)
    print('\ndata:', ls._data)
    print('\ndumping...')
    ls.dump()
    print('\ndata:', ls._data)
