#!/usr/bin/env python3

import sys
from pathlib import Path

def main():
    """ AoC 2024 Day 1 Part a. """
    inf = "01a-input.txt"
    left = []
    right = []
    f = Path(inf)
    if f.exists() and f.is_file():
        with f.open() as fd:
            lls = fd.readlines()
            for ll in lls:
                (a, b) = ll.strip().split("   ")
                left.append(int(a))
                right.append(int(b))
    else:
        print(f'{inf} does not exist')
    lsort = sorted(left)
    rsort = sorted(right)
    dist = 0
    for (l, r) in zip(lsort, rsort):
        dist += abs(l - r)
    print(dist)

if __name__ == '__main__':
    main()
