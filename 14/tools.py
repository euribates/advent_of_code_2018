#!/usr/bin/env python3

import collections


def is_sublist(inner_list, outer_list):
    delta = len(outer_list) - len(inner_list)
    if delta < 0:
        return -1
    length_ = len(inner_list)
    for index in range(delta+1):
        if outer_list[index:index+length_] == inner_list:
            return index
    return -1


class Recipes:
    
    def __init__(self, seed='37'):
        self.p0 = 0
        self.p1 = 1
        self.dl = [int(s) for s in seed]
        self.last_items = collections.deque(self.dl[:], maxlen=12)
        self.size = len(self.dl)

    def __iter__(self):
        return self
        
    def next(self):
        s = str(self.dl[self.p0] + self.dl[self.p1])
        for c in s:
            self.dl.append(int(c))
            self.last_items.append(int(c))
            self.size += 1
        self.p0 = (self.p0 + self.dl[self.p0] + 1) % self.size
        self.p1 = (self.p1 + self.dl[self.p1] + 1) % self.size
    
    def __str__(self):
        buff = []
        for i, item in enumerate(self.dl):
            if i == self.p0:
                buff.append('({})'.format(item))
            elif i == self.p1:
                buff.append('[{}]'.format(item))
            else:
                buff.append(str(item))
        return ' '.join(buff)

    def tail(self, limit, size=10):
        p = self.size - 12
        start = 0
        while p < limit:
            p += 1
            start += 1
        return ''.join([
            str(_)
            for _ in self.last_items
            ][start:start+size])


def find_after(limit, size=10):
    r = Recipes()
    max_size = limit + size
    while r.size < max_size:
        r.next()
    return r.tail(limit, size)

