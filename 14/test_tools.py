#!/usr/bin/env python3

import pytest
from tools import find_after

samples = [
    (5, '0124515891'),
    (9, '5158916779'),
    (18, '9251071085'),
    (2018, '5941429882'),
]

def _sample_id(param):
    return 'sample_{}_is_{}'.format(*param)

@pytest.fixture(params=samples, ids=_sample_id)
def sample(request):
    return request.param

def test_samples(sample):
    limit, target = sample
    assert find_after(limit) == target