#!/usr/bin/env python3

from tools import create_tree


def test_leaf_node():
    n = create_tree([0, 1, 99])
    assert n.n_sons == 0
    assert n.n_metadata == 1
    assert len(n.metadata) == 1
    assert n.metadata[0] == 99
    assert n.value() == 99
    print(n)


def test_value():
    n = create_tree([0, 3, 10, 11, 12])
    assert n.value() == 33


def test_value_index_out_of_limits():
    b = create_tree([1, 1, 0, 1, 99, 2])
    assert b.value() == 0


def test_value_sample():
    l = [int(x) for x in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()]
    root = create_tree(l)
    assert root.value() == 66 


def test_one_son():
    n = create_tree([1, 1, 0, 1, 99, 2])
    assert n.n_sons == 1
    assert len(n.sons) == 1
    son = n.sons[0]

    assert son.n_sons == 0
    assert son.n_metadata == 1
    assert len(son.metadata) == 1
    assert son.metadata[0] == 99
    assert son.n_sons == 0

    assert len(n.metadata) == 1
    assert n.metadata[0] == 2 

    print(n)
    print(n.sons[0])


def test_sample():
    l = [int(x) for x in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()]
    root = create_tree(l)
    print(root)
    for n in root.sons:
        print(n)
        for niece in n.sons:
            print(niece)


