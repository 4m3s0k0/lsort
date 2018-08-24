#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from os import mkdir, chdir, getcwd #---------#
from pickle import load, dump #---------------#
from os.path import exists, getsize, basename #
from collections import defaultdict #---------#


class LS:
    """
    IDEA FROM:
        GRAVITY AND FALLING OBJECTS
    ---------------------------------
    Numbers will go to their Levels
    List not sorted while we don't need it
    I will use builting sort function to sort numbers in level
    ---------------------------------
    EXP:
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
    """

    def __init__(self):
        self.LS = None
        self.LH = None
        self.LT = None
        self._ffp = 'position_levels.pickle'
        self._ffl = 'position_length.pickle'
        self._ffs = 'lsort.pickle'
        self._link = list(range(10))
        self._lsort = []
        self._ddict = defaultdict(list)
        self._gdict = defaultdict(list)
        self._saved = 'saved_data'
        self._llevels = defaultdict(dict)


    def __linked_levels(self):
        """
        One level has numbers from 0 to 9
        I will remove repeating numbers with adding 'T', or 'F'
        'T' -> True,  i already have numbers in self._link
        'F' -> False, length and items != self._link
        """
        F = True
        for keys in self._llevels:
            for key in self._llevels[keys]:
                item = self._llevels[keys][key]
                if len(item) == len(self._link):
                    if not set(self._link) ^ set(item):
                        self._llevels[keys][key] = ['T']
                        F = False
                if F:
                    item.sort()
                    self._llevels[keys][key] = ['F'] + item


    def __levels(self, _input):
        """
        make dict:  key = length of number,
                    value = numbers with length == key
        ---------------------------------
        make levels:keys = make dict[key],
                    key = item ot item[:-1],
                    value = item or item[-1]
        """
        # FILL DDICT
        ddict = defaultdict(list)
        for num in _input:
            ddict["{}".format(len(str(num)))].append(num)
        # USE DDICT FOR LEVELS
        for key in ddict.keys():
            for item in ddict[key]:
                item = str(item)
                try:
                    self._llevels[key][
                        '0' if len(item) == 1 else item[:-1]
                    ].append(int(item) if len(item) == 1 else int(item[-1]))
                except KeyError:
                    self._llevels[key][
                        '0' if len(item) == 1 else item[:-1]
                    ] = [int(item) if len(item) == 1 else int(item[-1])]
        # CLEAR DDICT
        ddict.clear()
        self.__linked_levels()


    def __make_dir(self):
        """
        Make directory to save logs and sorted list
        """
        if basename(getcwd()) != self._saved:
            if not exists(self._saved):
                mkdir(self._saved)
            chdir(self._saved)


    def __parse_log(self):
        """
        Get position of (length and levels), (make dict and make levels) with list slising
        """
        # MAKE DICT
        for key in self.LH:
            start, stop = self.LH[key]
            self._ddict[key] = self.LT[start:stop]
        # MAKE LEVELS
        for lengk in self.LS.keys():
            for key in self.LS[lengk]:
                start, stop = self.LS[lengk][key]
                self._llevels[lengk][key] = [
                    item if len(str(item)) == 1 else int(str(item)[-1]) for item in self._ddict[lengk][start:stop]
                ]
        self.__linked_levels()
        # REMOVE LOADED FILES
        self.LS = None
        self.LH = None
        self.LT = None
        # TO MAKE SURE THAT LOG SUCCESFULLY PARSED
        # print(self._llevels)


    def _append(self, _input):
        """
        :arg:   _input -> integer or list of integers
        ---------------------------------
        1st time _append: creates linked list
        2nd time _append: appends to the linked list
        """
        # LS SORTING ONLY INTEGERS
        if isinstance(_input, (str, bool, float)):
            assert isinstance(_input, int), 'Need integer, or list of integers'
        # FIRST AND SECOND CALLS
        if not self._llevels:
            self.__levels(_input)
        else:
            if isinstance(_input, int):
                _input = [_input]
            # APPEND TO LINKED LIST
            for item in _input:
                item = str(item)
                meti = '0' if len(item) == 1 else item[:-1]
                leni = str(len(item))
                if meti in self._llevels[leni].keys():
                    if self._llevels[leni][meti][0] == 'T':
                        newi = self._link + [int(item) if len(item) == 1 else int(item[-1])]
                        newi.sort()
                        self._llevels[leni][meti] = newi
                    else:
                        newi = [int(item[-1])] + self._llevels[leni][meti][1:]
                        newi.sort()
                        self._llevels[leni][meti][1:] = newi
                else:
                    self._llevels[leni][meti] = ['F', int(item[-1])]


    def _get_dict(self, logit=False):
        """
        Return dict:key = length of number,
                    value = numbers with length == key
        """
        # _gdict = {} NOT HELPING, I NEED CLEAR IT AFTER 1st CALL
        if self._gdict:
            self._gdict.clear()
        # FOR LOG AND KEYS
        log = defaultdict(dict)
        link = list(range(10))
        kkey = {}
        skey = []
        position = 0
        # SORT DICT KEYS
        for keys in self._llevels.keys():
            ikey = int(keys)
            skey.append(ikey)
            kkey[ikey] = [int(each) for each in self._llevels[keys].keys()]
        skey.sort()
        # FILL DICT
        for gkeys in skey:
            kkey[gkeys].sort()
            for lengk in kkey[gkeys]:
                gkeys = str(gkeys)
                lengk = str(lengk)
                pposi = 0 if position == 0 else position
                if self._llevels[gkeys][lengk][0] == 'T':
                    self._gdict[gkeys].extend(
                        [int('{}{}'.format(lengk, each)) for each in link]
                    )
                    if logit:
                        log[gkeys][lengk] = (pposi, pposi + 10)
                        position = pposi + 10
                else:
                    self._gdict[gkeys].extend(
                        [int('{}{}'.format(lengk, each)) for each in self._llevels[gkeys][lengk][1:]]
                    )
                    if logit:
                        position += len(self._llevels[gkeys][lengk][1:])
                        log[gkeys][lengk] = (pposi, position)
            position = 0
        # WRITE LOG
        if logit:
            with open(self._ffp, 'wb') as file_for_position:
                dump(log, file_for_position)
            del log
        # FLAG LOGIT ONLY FOR SAVING POSITION
        if not logit:
            return self._gdict


    def _get_list(self, logit=False):
        """
        Return sorted list
        """
        # CLEAR TO SAVE NEW
        if self._lsort:
            self._lsort.clear()
        # FOR LOG
        log = defaultdict(list)
        gdict = self._get_dict()
        position = 0
        # FILL LIST
        for key in gdict.keys():
            self._lsort.extend(gdict[key])
            if logit:
                pposi = 0 if position == 0 else position
                position += len(gdict[key])
                log[key] = (pposi, position)
        # WRITE LOG
        if logit:
            with open(self._ffl, 'wb') as file_for_position:
                dump(log, file_for_position)
            del log
        # RETURN TO USER
        return self._lsort


    def _clear(self, _all=False):
        """
        _get_dict and _get_list returns data but can't clear
        """
        self._gdict.clear()
        self._lsort.clear()
        if not all:
            return None
        self._ddict.clear()
        self._llevels.clear()


    def _save(self, filename=False):
        """
        :arg:   filename -> name for sorted list
        ---------------------------------
        :Save:  LENGTHS         (position_length.pickle),
                LEVELS          (position_levels.pickle)
                AND SORTED LIST (default: lsort.pickle)
        """
        if not filename:
            filename = self._ffs
        # CHANGE DIR TO SAVE (LENGTHS, LEVELS, LSORT)
        self.__make_dir()
        # SAVE LOG LEVELS 
        self._get_dict(logit=True)
        # SAVE LOG LENGTH, AND RETURN SORTED LIST
        lsort = self._get_list(logit=True)
        # SAVE SORTED LIST
        with open(filename, 'wb') as file_for_save:
            dump(lsort, file_for_save)
        # REMOVE LIST
        del lsort
        self._clear()


    def _load_with_logs(self, filename=False):
        """
        Make self._llevels with saved logs and sorted list
        ---------------------------------
        >>> exists(itemfiles)
        [True, True, True]
        >>> getsize('position_levels.pickle')
        40
        >>> # if size == 0
        >>> with open('position_levels.pickle') as ffl: levels = load(ffl)
        ???Error, Ran out of input
        """
        if not filename:
            filename = self._ffs
        # CHANGE DIRECTORY
        self.__make_dir()
        FILES = (self._ffp, self._ffl, self._ffs)
        # LOAD DATA AND LOGS
        if all([exists(ifs) for ifs in FILES]):
            for each in FILES:
                if getsize(each) == 0:
                    raise BaseException('File "{}" is empty'.format(each))
            del FILES
            # POSITION_LEVELS.PICKLE
            with open(self._ffp, 'rb') as ffp:
                self.LS = load(ffp)
            # POSITION_LENGTH.PICKLE
            with open(self._ffl, 'rb') as ffl:
                self.LH = load(ffl)
            # LSORT.PICKLE
            with open(self._ffs, 'rb') as ffs:
                self.LT = load(ffs)
        # PARSE DATA AND LOGS
        self.__parse_log()


if __name__ == "__main__":
    pass
    # lsort = LS()
    # lsort._append([1, 5, 10])
    # lsort._append([8, 9, 11, 32, 45])
    # print(lsort._get_dict())
    # print(lsort._get_list())
    # lsort._save()
    # lsort._clear(True)
    # lsort._load_with_logs()
