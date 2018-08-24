#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from time import time #----#
from lsort import LS #-----#
from random import randint #


""" MAYBE I NEED TO UPGRADE MY LSORT LOGIC
"""


ft = (False, True)
slj = 857942
line = '-' * 45
nran = (0, 700_000)
lsort = LS()
allst = []


"""
SORT TIME ,-__-,
---------------------------------------------
builting sort, sorting in place, so it has already appended list
lsort firt needs to append list to levels, and sort it
---------------------------------------------
WITH APPEND:
    lsort count: 857942, in time: 2.3466341495513916
    bsort count: 857942, in time: 0.5055882930755615
WITHOUT:
    lsort count: 857942, in time: 0.6501996517181396
    bsort count: 857942, in time: 0.5054934024810791
---------------------------------------------


def level_sort(_appended):
    st = time()
    if not _appended:
        lsort._append(allst)
    lsort._get_list()
    print('lsort count: {}, in time: {}'.format(len(allst), time() - st))


def builting_sort():
    st = time()
    allst.sort()
    print('bsort count: {}, in time: {}'.format(len(allst), time() - st))


def check_time():
    for i in ft:
        allst.extend([randint(*nran) for _ in range(slj)])
        if i:
            lsort._append(allst)
        level_sort(i)
        builting_sort()
        lsort._clear(_all=True)
        allst.clear()


check_time()
"""


"""
APPEND TO LEVELS ,-__-,
---------------------------------------------
lsort, -> _llevels['length']['level'].append(), 1.
list nah sorted, maybe for loop found level 63755 begin of the list
---------------------------------------------
WITH _APPEND:
    lsort append: 63755, in time: 1.6395409107208252
    bsort append: 63755, in time: 0.0186617374420166
WITHOUT:
    lsort append: 63755, in time: 1.4543533325195312e-05
    bsort append: 63755, in time: 0.008521556854248047
---------------------------------------------


def level_insert(fnd, _appended):
    st = time()
    if not _appended:
        lsort._append(allst)
    fnd = str(fnd)
    lsort._llevels[
        str(len(fnd))]['0' if len(fnd) == 1 else fnd[:-1]
    ].append(int(fnd) if len(fnd) == 1 else int(fnd[-1]))
    print('lsort append: {}, in time: {}'.format(fnd, time() - st))


def builting_insert(fnd):
    kks = list(range(fnd))[::-1]
    st = time()
    for idx, _ in enumerate(range(fnd)):
        try:
            mnew = allst.index(kks[idx])
        except ValueError:
            pass
        else:
            allst.insert(mnew, fnd)
            break
    print('bsort append: {}, in time: {}'.format(fnd, time() - st))


def check_time():
    fit = randint(*nran)
    for i in ft:
        allst.extend([randint(*nran) for _ in range(slj)])
        if i:
            lsort._append(allst)
        level_insert(fit, i)
        builting_insert(fit)
        lsort._clear(_all=True)
        allst.clear()


check_time()
"""


"""
GET LEVELS ,-__-,
---------------------------------------------
get _llevels['6']['38444'] -> 2., ohhh c'mon, you shouldn't check hole list
---------------------------------------------
WITH _APPEND:
    lsort find level: 384441, [384442 ... 384443] in time: 1.650613784790039
    bsort find level: 384441, [384444 ... 384443] in time: 0.04118609428405762
WITHOUT:
    lsort find level: 384441, [384442 ... 384443] in time: 2.1696090698242188e-05
    bsort find level: 384441, [384444 ... 384443] in time: 0.040830373764038086
---------------------------------------------


def level_pattern(fnd, _appended):
    st = time()
    if not _appended:
        lsort._append(allst)
    fnd = str(fnd)
    msn = '0' if len(fnd) == 1 else fnd[:-1]
    fided = [int(msn + str(i)) for i in lsort._llevels[str(len(fnd))][msn][1:]]
    print('lsort find level: {}, {} in time: {}'.format(fnd, fided, time() - st))


def list_pattern(fnd):
    st = time()
    msn = '0' if len(str(fnd)) == 1 else str(fnd)[:-1]
    start, stop = int(msn + '0'), int(msn + '9')
    fided = []
    for i in allst:
        if i >= start and i <= stop:
            fided.append(i)
    print('bsort find level: {}, {} in time: {}'.format(fnd, fided, time() - st))


def check_time():
    allst.extend([randint(*nran) for _ in range(slj)])
    fit = randint(*nran)
    for i in ft:
        if i:
            lsort._append(allst)
        level_pattern(fit, i)
        list_pattern(fit)
        lsort._clear(_all=True)


check_time()
"""
