#!/usr/bin/env python3

import itertools


def read_input(filename='input.txt'):
    with open(filename, 'r') as f:
        for line in f:
            for x in line.split():
                yield int(x)


def get_names(letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'):
    for a, b in itertools.product(letters, letters):
        yield '{}{}'.format(a, b)


def as_human_list(l):
    n = len(l)
    if n == 0:
        return ''
    elif n == 1:
        return str(l[0])
    else:
        *head, tail = l
        return '{heads} and {tail}'.format(
            heads=', '.join([str(_) for _ in head]),
            tail=tail,
            )


class Node:

    def __init__(self, name, n_sons, n_metadata):
        self.name = name
        self.n_sons = n_sons
        self.sons = []
        self.n_metadata = n_metadata
        self.metadata = []

    def __str__(self):
        return 'Node {} metadata is {} has {} sons ({})'.format(
            self.name,
            as_human_list(self.metadata),
            self.n_sons,
            as_human_list([_.name for _ in self.sons]),
            )

    def value(self):
        assert self.n_metadata == len(self.metadata)
        assert self.n_sons == len(self.sons)
        if self.sons:
            acc = 0
            for index in self.metadata:
                if 0 < index <= self.n_sons:
                    acc += self.sons[index-1].value()
            return acc
        else:
            return sum(self.metadata)


def create_tree(seq):
    names = get_names()
    seq = iter(seq)
    return _recursive_create_tree(seq, names)


def _recursive_create_tree(seq, names):
    name = next(names)
    n_sons = next(seq)
    n_metadata = next(seq)
    node = Node(name, n_sons, n_metadata)
    for _ in range(n_sons):
        node.sons.append(_recursive_create_tree(seq, names))
    for _ in range(n_metadata):
        node.metadata.append(next(seq))
    return node

