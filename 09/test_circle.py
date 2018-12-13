#!/usr/bin/env python3

import pytest

from tools import play


samples = [
    (9, 25, 32),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305),
    ]


def ids(t):
    return '{} players {} points max. score {}'.format(*t)


@pytest.fixture(params=samples, ids=ids)
def sample(request):
    return request.param


def test_sample(sample):
    num_players, points, target = sample
    sb = play(num_players, points)
    winner = max(sb, key=lambda k: sb[k])
    assert sb[winner] == target
