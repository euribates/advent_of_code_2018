#!/usr/bin/env python3

import collections

class Recipes:
    
    def __init__(self, seed='37'):
        self.p0 = 0
        self.p1 = 1
        self.dl = collections.deque(seed)
        self.size = 2
        
    def next(self):
        s = str(int(self.dl[self.p0]) + int(self.dl[self.p1]))
        for c in s:
            self.dl.append(c)
            self.size += 1
        self.p0 = (self.p0 + int(self.dl[self.p0]) + 1) % self.size
        self.p1 = (self.p1 + int(self.dl[self.p1]) + 1) % self.size
    
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
        buff = []
        for index in range(limit, limit+size):
            buff.append(self.dl[index])
        return ''.join(buff)

def find_after(limit, size=10):
    r = Recipes()
    max_size = limit + size
    while r.size < max_size:
        r.next()
    return r.tail(limit, size)