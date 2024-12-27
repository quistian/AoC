#!/usr/bin/env python3

from pathlib import Path
from itertools import pairwise
from rich import print

Debug = False
Debug = True

def diffs(v):
    dfs = []
    for i,j in pairwise(v):
        dfs.append(int(j) - int(i))
    return dfs

def asc_or_desc(v):
    all_neg = all(i < 0 for i in v)
    all_pos = all(i > 0 for i in v)
    return all_neg or all_pos

def within_bounds(v):
    return all(abs(i) < 4 and abs(i) > 0 for i in v)


def main():
    inf = '02.reports'
    p = Path(inf)
    with p.open() as fd:
        lines = [line.rstrip() for line in fd]
        cnt = 0
        for line in lines:
            toks = line.split(' ')
            dfs = diffs(toks)
            good = asc_or_desc(dfs) and within_bounds(dfs)
            if good:
                cnt += 1
                if Debug:
                    print('good:',toks, dfs)
        print(cnt)

if __name__ == '__main__':
    main()
