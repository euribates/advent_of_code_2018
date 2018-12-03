#!/usr/bin/env python

import pytest
import tools
from collections import defaultdict


def test_parse():
    claim = tools.parse('#1 @ 2,3: 5x4')
    assert claim.id == 1
    assert claim.left == 2
    assert claim.top == 3
    assert claim.width == 5
    assert claim.height == 4


def test_iterator():
    claim = tools.parse('#1 @ 2,3: 5x4')
    for coord in claim:
        print(coord)


def test_print_mapa():
    mapa = defaultdict(int)
    claim = tools.parse('#1 @ 2,3: 5x4')
    for (x, y) in claim:
        mapa[(x, y)] += 1
    tools.print_mapa(mapa)


def test_sample():
    inputs = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]
    mapa = defaultdict(int)
    for s in inputs:
        claim = tools.parse(s)
        for (x, y) in claim:
            mapa[(x, y)] += 1
    tools.print_mapa(mapa)


if __name__ == "__main__":
    pytest.main()
