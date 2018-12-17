#!/usr/bin/env python3

from tools import CellMap


def test_serial_18():
    m = CellMap(18)
    acc = 0
    for y in range(45, 48):
        for x in range(33, 36):
            print(m.power(x, y), end=' ')
            acc += m.power(x, y)
        print()

    assert acc == 29
    assert m.power3x3(33, 45) == 29
    assert m.powerNxN(33, 45, 3) == 29


def test_serial_42():
    m = CellMap(42)
    acc = 0
    for y in range(61, 64):
        for x in range(21, 24):
            acc += m.power(x, y)
    assert acc == 30
    assert m.power3x3(21, 61) == 30
    assert m.powerNxN(21, 61, 3) == 30
