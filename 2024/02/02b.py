#!/usr/bin/env python3

from pathlib import Path
from itertools import pairwise, dropwhile, filterfalse
from rich import print

Debug = True
Debug = False

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

def is_safe_with_removal(r):
    for i in range(len(r)):
        tmp = r.copy()
        del tmp[i]
        if is_safe(tmp):
            return True
    return False

def main():
    fname = '02.reports'
    cwd = Path.cwd()
    print(cwd)
    inf = Path(fname)
    with inf.open() as fd:
        lines = [line.rstrip() for line in fd]
        cnt1 = 0
        cnt2 = 0
        for line in lines:
            toks = line.split(' ')
            report = [int(t) for t in toks]
            if is_safe(report):
                cnt1 += 1
            elif is_safe_with_removal(report):
                cnt2 += 1
    print(cnt1, cnt2, cnt1+cnt2)


if __name__ == '__main__':
    main()