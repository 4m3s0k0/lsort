# lsort -> LEVEL SORT
CALLABLE METHODS: test_pic.png
```
>>> test1 = [1, 5, 10]
>>> lsort = LS()
>>> lsort._append(test1)
#levels: defaultdict(<class 'dict'>, {
                            '1': {
                                '0': ['F', 1, 5]
                            },
                            '2': {
                                '1': ['F', 0]
                            }
                        }
                    )

>>> test2 = [8, 9, 11, 32, 45]
>>> lsort._append(test2)
#levels: defaultdict(<class 'dict'>, {
                            '1': {
                                '0': ['F', 1, 5, 8, 9]
                            },
                            '2': {
                                '1': ['F', 0, 1],
                                '3': ['F', 2],
                                '4': ['F', 5]
                            }
                        }
                    )

>>> print(lsort._get_dict())
defaultdict(<class 'list'>, {'1': [1, 5, 8, 9], '2': [10, 11, 32, 45]})

>>> print(lsort._get_list())
[1, 5, 8, 9, 10, 11, 32, 45]

>>> lsort._save(filename) # default filename = 'lsort.pickle'
# created file: position_length.pickle
# created file: position_levels.pickle
# created file: lsort.pickle

>>> lsort._clear(_all=True) # default _all = False, will clear only (_get_dict, _get_list)

>>> lsort._load_with_logs(filename)
```
HOW SHOULD IT WORK:
```
Numbers will go to their Levels
List not sorted while I don't need it
I will use builting sort function to sort numbers in level and keys of dict


dict = {
    -------------------------------------
    'len(n)': [n]       | SORT(N)
    -------------------------------------
    '1': [0 ... 9],     | LSORT(dct['1'])
            0lvl        |
    '2': [10 ... 99],   | LSORT(dct['2'])
            0lvl        |
            9lvl        |
    '3': [100 ... 999]  | LSORT(dct['3'])
            0lvl        |
            n...        |
            99lvl       |
    ------------------------------------
}

##### (1, 6) -> [0, 1, 2, 4, 7, 3]
##### (index(min(level[keys][key][0])), len(level[keys][key]))
position = {
    '1': {
        # position from 0 to 9
        '0': 0 ... len(n)
        '1': len(key('0')) + 0 ... len(n)
    }
    '2': {
        # position from 10, 99
    }
}


--------------------------------- LSORT ---------------------------------
1, 8, 2, 3, 10, 4, 7, 5, 6, 22, 13  |  0level: len(n) == 1
----------------------------------  |  -------------------
1level-------0...................3  |  1level: len(n) == 2 and startswith 1: 10, 11 ...
2level-----------------------2----  |  2level: len(n) == 2 and startswith 2: 20, 21 ...


----------------------------------
1, 2, 3, 4, 5, 6, 7, 8

        1level: (0 <=> 3): 10, 13
----------------------------------
1, 2, 3, 4, 5, 6, 7, 8, 10, 13

        2level: (2): 22
----------------------------------
1, 2, 3, 4, 5, 6, 7, 8, 10, 13, 22


----------------------------------
append(n) -> dict[len(n)] -> lst[n] -> LSORT:GET_LEVEL -> SORT ONLY LEVEL
exp: 45
append(45) > dict['2'] > '2': [10 ... 99] > LSORT:LEVEL=4 == [40 ... 49]

# FULL_LIST -> dict['1'] + dict['2']
# LEVEL:(45, 89)


ALL LEVELS HAVE NUMBERS 0 ... 9
WE CAN MAKE LINK TO EXIST LEVEL WITH NUMBERS 0 ... 9

EXP, if we have sorted list from 0 to 20:
levels = {
    '1': {
        '0': [False, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 0 + 0 = 0, [True, 'S']
        '1': [True, '0']    # linked to levels with len 1 | dict with len 1
        '2': [True, '0']    # how to fill 1level:
    }                       # m = levels[len(n)][str(n)[:-1]][0]
}
#                            if m:
#                                s = levels[len(n)][str(n)[:-1]] # '10' -> '1'
#                                # '1' + '0' == 10
#                                # [False, 10 ... 19]
#                                levels[len(n)][str(n)[-1]] = [False] + [
#                                    int(len(n) + str(i)) for i in levels[s][1:]
#                                ]


+-------+-------------------------------------------------------+
| steps | actions                                               |
----------------------------------------------------------------+
| s1:     list: [0 .... 48565]                                  |
|         input n = 856                                         |
+---------------------------------------------------------------+
| s2:     length(n) = str(3)                                    |
|         call levels['3']                                      |
+---------------------------------------------------------------+
| s3:     level = str(n)[:-1] = '85'                            |
|         new_n = str(n)[-1] = int('6')                         |
+---------------------------------------------------------------+
| s4:     call and append like: levels['3']['85'].append(new_n) |
+---------------------------------------------------------------+

>>> print(levels['3']['85'])
[4, 1, 5, 8, 0, 6] -> 6 == new_n
```
