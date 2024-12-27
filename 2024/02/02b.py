#!/usr/bin/env python3

from pathlib import Path
from itertools import pairwise, dropwhile, filterfalse
from rich import print

Debug = True
Debug = False


def diffs(v):
    dfs = []
    for i,j in pairwise(v):
        dfs.append(int(j) - int(i))
    return dfs


def asc_or_desc(v):
    return is_asc(v) or is_desc(v)


def within_bounds(v):
    return all(abs(i) < 4 and abs(i) > 0 for i in v)

def is_asc(v):
    return all(i>0 for i in v)

def is_desc(v):
    return all(i<0 for i in v)
    
def is_safe(v):
    return asc_or_desc(v) and within_bounds(v)

def is_safe_save_one(v):
    cnt = 0
    for i in range(len(v)-2):
       tmp = v.copy()
       tmp.pop(i)
       if is_safe(tmp):
           cnt += 1
    tmp = v.copy()
    tmp.pop()
    if is_safe(tmp):
        cnt += 1
    if cnt == 1:
        return True
    else:
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
            dfs = diffs(toks)
            if is_safe(dfs):
                cnt1 += 1
            elif is_safe_save_one(dfs):
                cnt2 += 1
        print(cnt1, cnt2, cnt1 + cnt2)


if __name__ == '__main__':
    main()