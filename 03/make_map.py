#!/usr/bin/env python3

import tools
from PIL import Image
from collections import defaultdict


if __name__ == "__main__":
    mapa = defaultdict(int)
    max_cols = 0
    max_rows = 0
    for claim in tools.read_input(transform=tools.parse):
        max_cols = max(max_cols, claim.left+claim.width)
        max_rows = max(max_rows, claim.top+claim.height)
        for (x, y) in claim:
            mapa[(x, y)] += 1
    img = Image.new('RGB', (max_cols, max_rows), color=(255, 255, 255))
    colors = [
        (240, 240, 240),
        (103, 103, 224),
        (93, 93, 208),
        (83, 83, 176),
        (63, 63, 136),
        (53, 53, 112),
        (43, 43, 88),
        (33, 33, 64),
        ]
    for x in range(max_cols):
        for y in range(max_rows):
            v = mapa[(x, y)]
            color = colors[v]
            img.putpixel((x, y), color)
    for (x, y) in tools.Claim('#124 @ 408,411: 18x10'):
        img.putpixel((x, y), (255, 32, 32))
    img.save("patches.png")
