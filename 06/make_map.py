#!/usr/bin/env python3

import tools
from PIL import Image


def dot(img, x, y, color, fat=True):
    if fat:
        img.putpixel((x-1, y-1), color)
        img.putpixel((x-1, y), color)
        img.putpixel((x-1, y+1), color)
        img.putpixel((x-1, y), color)
    img.putpixel((x, y), color)
    if fat:
        img.putpixel((x+1, y), color)
        img.putpixel((x+1, y-1), color)
        img.putpixel((x+1, y), color)
        img.putpixel((x+1, y+1), color)


if __name__ == "__main__":
    m = tools.ColorMap('input.txt')
    img = Image.new('RGB', (m.max_x+1, m.max_y+1), color=(255, 255, 255))
    m.analyze()
    for (x, y) in m.plane:
        name = m.plane[(x, y)]
        if name != '0':
            color = m.color[name]
            dot(img, x, y, color, fat=False)
    for name in m.kernel:
        x, y = m[name]
        color = m.color[name]
        dot(img, x, y, color, fat=False)
    img.save("map.png")
