#!/usr/bin/env python3

import pytest
from tools import is_sublist


def test_is_sublist():
    assert is_sublist([2,3], [1,2,3,4]) == 1


def test_is_sublist_false():
    assert is_sublist([2,7], [1,2,3,4]) == -1


def test_is_sublist_at_start():
    assert is_sublist([1,2], [1,2,3,4]) == 0


def test_is_sublist_at_end():
    assert is_sublist([3, 4], [1,2,3,4]) == 2


def test_is_sublist_wrong_parameters_order():
     assert is_sublist([1,2,3,4], [3, 4]) is -1


def test_is_sublist_over():
    assert is_sublist([3, 4, 5], [1,2,3,4]) is -1


def test_is_sublist_uinder():
    assert is_sublist([0, 1, 2], [1,2,3,4]) is -1

