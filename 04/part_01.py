#!/usr/bin/env python

import tools
import collections

if __name__ == '__main__':
    i = 0
    by_date = collections.defaultdict(list)
    for (a, b, c) in sorted(tools.read_input(transform=tools.parse_log)):
        print(a, b, c)
        day = a[5:10]
        by_date[day].append((a, b, c))
    for k in by_date:
        print(k, len(by_date[k]), by_date[k][0])
