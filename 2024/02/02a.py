#!/usr/bin/env python3

from pathlib import Path
from itertools import pairwise
from rich import print

Debug = False
Debug = True

def diffs(r):
    dfs = []
    for i,j in pairwise(r):
        dfs.append(j - i)
    return dfs

def asc_or_desc(r):
    return is_asc(r) or is_desc(r)

def is_asc(r):
    d = diffs(r)
    return all(i > 0 for i in d)

def is_desc(r):
    d = diffs(r)
    return all(i < 0 for i in d)

def within_bounds(r):
    d = diffs(r)
    return all(abs(i) < 4 and abs(i) > 0 for i in d)

def is_safe(r):
    return asc_or_desc(r) and within_bounds(r)


def main():
    inf = '02.reports'
    p = Path(inf)
    with p.open() as fd:
        lines = [line.rstrip() for line in fd]
        cnt = 0
        for line in lines:
            toks = line.split(' ')
            report = [int(t) for t in toks]
            good = asc_or_desc(report) and within_bounds(report)
            if good:
                cnt += 1
                if Debug:
                    print('good:',report, diffs(report))
        print(cnt)

if __name__ == '__main__':
    main()
