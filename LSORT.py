#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from collections import defaultdict


class LS:
    """
    not now
    """
    # __slots__ = [_make_level]

    def __init__(self):
        self.data = defaultdict(list)
        self.levels = defaultdict(list)


    def _store_level(self, strlen, n, start, end):
        """
        :args:> strlen:     self.data['len(str(n))']
                str(n)[0]:  0l, 1l
                start/end:  (1, 6) == [1 ... 9, 15]: get(nlevel[p[0]:p[1]])
        ---------------------------------------------
        :exp:>  levels = {
                    '1': {
                        '0l': (1, 6),
                    }
                }
        ----------------------------------------------
        """
        # self.levels[dlength][nlevel] = nposition
        # self.levels[strlen][str(n)[0]] = (start, end)
        # strlen: 2 -> 45, [:-1] -> 4, 4level
        # self.levels[strlen][str(n)[:-1]] = (start, end)
        # if not self.levels[strlen][str(n)[:-1]]:
        #     self.levels[strlen][str(n)[:-1]
        pass

    def _append(self, n):
        """
        |1level| + |2level| > pos==1:(start_1level, start_2level), 2:(start__2level, ... )

        get len(n) -> dict[len(n)] -> get level of n -> find position for nlevel\
        append to level -> upgrade position n and levels after n
        """
        pass

    def _sort_level(self):
        """
        elems: 10, 10, 10
        n = 312, level: 31
        """
        for key in self.data.keys():
            for level in self.data[key]:

    def _make_level(self, nlist):
        """
        'len(n)': [n ... n],     | LSORT(dct['1'])
        """
        sitem = str(len(item))
        for item in nlist:
            if not self.data[sitem]:
                self.data[sitem] = []
                self.levels[sitem] = {"{}".format(sitem[:-1]): []}
            self.data[sitem].append(item)
            self.levels[sitem][sitem[:-1]].append(item)

    def _get_level(self, n):
        """
        return (start, end)
        """
        return self.levels[strlen][str(n)[:-1]]

    def _upgrade_position(self, level, stop):
        """
        position:stop, (s, s) -> [s, s, s, s]
        dict to list: [1, 2, 3, 12, 15, 10]
                      |1level |+| 2level  |
        |1level| + |2level| > pos==1:(start_1level, start_2level), 2:(start__2level, ... )
        """
        pass

    def _data_list(self, n):
        """
        dict = {
            'len(str(n))': [n]
        }
        """
        strlen = "{}".format(len(str(n)))
        if not self.data[strlen]:
            self.data[strlen] = []
            # self._make_level(strlen, n, (1, 1))
        self.data[strlen].append(n))
        # self._make_level(strlen, n, (1, 1))
