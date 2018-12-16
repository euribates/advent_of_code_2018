#!/usr/bin/env python3

from tools import Scale
from tools import Vector2


def test_scale_100x100():
    scale = Scale(
        left_top=Vector2(0, 0),
        right_bottom=Vector2(100, 100),
        width=1000,
        height=1000,
        )
    assert scale(Vector2(0, 0)) == Vector2(0, 0)
    assert scale(Vector2(50, 50)) == Vector2(500, 500)
    assert scale(Vector2(100, 100)) == Vector2(1000, 1000)
