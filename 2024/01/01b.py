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
    dist = 0
    for l in left:
        cnt = 0
        for r in right:
            if r == l:
                cnt = cnt + 1
        dist += l * cnt
    print(dist)

if __name__ == '__main__':
    main()
