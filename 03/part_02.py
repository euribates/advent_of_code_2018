#!/usr/bin/env python3

import tools
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

    # tools.print_mapa(mapa, max_cols, max_rows)
    count = 0
    for claim in tools.read_input(transform=tools.parse):
        if all([mapa[(x, y)] == 1 for (x, y) in claim]):
            solution = claim
            count += 1
    assert count == 1
    print(f"Solution for part 2: {solution.id}")
