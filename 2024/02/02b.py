#!/usr/bin/env python3

from pathlib import Path
from itertools import pairwise, dropwhile, filterfalse
from rich import print

def diffs(v):
    dfs = []
    for i,j in pairwise(v):
        dfs.append(int(j) - int(i))
    return dfs

def one_out_of_bound(v):
    v_prime = []
    vprime = dropwhile(lambda x: abs(x) == 0 or abs(x) > 3, v)
    if (len(v) - len(vprime)) == 1 and asc_or_desc(vprime):
        return vprime
    else:
        return v

def asc_or_desc(v):
    all_neg = all(i <= 0 for i in v)
    all_pos = all(i >= 0 for i in v)
    return all_neg or all_pos

def within_bounds(v):
    good = all(abs(i) < 4 and abs(i) > 0 for i in v)
    return good


def main():
    inf = '02a.reports'
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
                print(toks, dfs)
                print()
        print(cnt)

if __name__ == '__main__':
    main()
