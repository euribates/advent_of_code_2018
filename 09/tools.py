#!/usr/bin/env python3

import itertools
import collections


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Circle:

    def __init__(self):
        self.zero = self.current = Node(0)
        self.current.left = self.current
        self.current.right = self.current
        self.size = 1

    def forward(self):
        self.current = self.current.right

    def backward(self):
        self.current = self.current.left

    def add(self, n):
        node = Node(n)
        pivot = self.current.right
        self.current.right = node
        node.left = self.current
        node.right = pivot
        pivot.left = node
        self.size += 1
        self.current = node

    def remove(self):
        ln = self.current.left
        rn = self.current.right
        ln.right = rn
        rn.left = ln
        self.current.left = self.current.right = None
        self.current = rn
        self.size -= 1

    def play(self, n):
        if n % 23 == 0:
            score = n
            for i in range(7):
                self.backward()
            score += self.current.value
            self.remove()
            return score
        else:
            self.forward()
            self.add(n)
            return 0

    def __str__(self):
        n = self.zero
        buff = [n]
        for i in range(self.size-1):
            n = n.right
            buff.append(n)
        return ' '.join([
            '({})'.format(n.value) if n == self.current else str(n.value)
            for n in buff
            ])


def play(num_players, points):
    steps = points
    circle = Circle()
    players = list(range(num_players))
    get_player = itertools.cycle(players)
    scoreboard = collections.defaultdict(int)
    for i in range(1, steps+1):
        player = next(get_player)
        score = circle.play(i)
        scoreboard[player] += score
    return scoreboard
