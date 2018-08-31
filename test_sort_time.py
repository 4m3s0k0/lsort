#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from time import time #-----#
from lsort import LevelSort #
from random import randint ##


ft = (False, True)
ls = LevelSort()
allst = []


"""
SORT TIME:  (ADD to lsort, GET from lsort)
---------------------------------------------
WITH ADD AND GET:
    lsort count: 857942, in time: 2.308032274246216
    bsort count: 857942, in time: 0.48810696601867676
---------------------------------------------
WITHOUT ADD AND WITH GET:
    lsort count: 857942, in time: 0.7055761814117432
    bsort count: 857942, in time: 0.48944544792175293
---------------------------------------------
WITHOUT ADD AND GET:
    lsort count: 857942, in time: 0.08258318901062012
    bsort count: 857942, in time: 0.5056655406951904
---------------------------------------------


def level_sort(_appended):
    # st = time()
    # if not _appended:
    #     ls._add(allst)
    m = ls._get()
    st = time()
    m.sort()
    print('lsort count: {}, in time: {}'.format(len(allst), time() - st))


def builting_sort():
    st = time()
    allst.sort()
    print('bsort count: {}, in time: {}'.format(len(allst), time() - st))


# def check_time():
#     for i in ft:
#         allst.extend([randint(0, 700000) for _ in range(857942)])
#         if i:
#             ls._add(allst)
#         level_sort(i)
#         builting_sort()
#         ls._new()
#         allst.clear()

def check_time():
    allst.extend([randint(0, 700000) for _ in range(857942)])
    ls._add(allst)
    level_sort(False)
    builting_sort()


check_time()
"""
