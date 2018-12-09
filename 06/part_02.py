#!/usr/bin/env python3

from PIL import Image
import tools
import collections

def get_distances(color_map, x, y):
    return [
        tools.distance((x, y), (x1, y1))
        for x1, y1 in color_map.kernel.values()
        ]


if __name__ == '__main__':
    limit = 10000
    m = tools.ColorMap('input.txt')
    plane = collections.defaultdict(int)
    acc = 0
    for x in range(0, m.max_x+1):
        for y in range(0, m.max_y+1):
            if sum(get_distances(m, x, y)) < limit:
                plane[(x, y)] = 1
                acc += 1
    img = Image.new('RGB', (m.max_x+1, m.max_y+1), (0,0,0))
    for x in range(0, m.max_x+1):
        for y in range(0, m.max_y+1):
            if plane[(x, y)]:
                img.putpixel((x, y), (56, 78, 223))
    img.save('map_part_2.png')
        # print()
    # assert get_distances(m, 4, 3) == [5, 6, 4, 2, 3, 10]
    solution = acc
    print(f'Solution of part 2 is {solution}')
