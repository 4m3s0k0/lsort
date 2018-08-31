# lsort -> LEVEL SORT
```
### file to read: .idea


>>> ls = LevelSort()
>>> print(ls.__doc__)

    Container like, ten (10) with nteens:
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


### script: test_sort_time.py

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
```
