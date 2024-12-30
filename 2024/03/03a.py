#!/usr/bin/env python3

import re
import sys
from pathlib import Path

def main():
    """ AoC 2024 Day 1 Part a. """
    inf = "03.input"
    f = Path(inf)
    if f.exists() and f.is_file():
        with f.open() as fd:
            instr = fd.read()
    target = r'mul\((\d+),(\d+)\)' 
    ll = re.findall(target, instr)
    sum = 0
    for duo in ll:
        (i, j) = duo
        sum += int(i) * int(j)
    print(sum)


if __name__ == '__main__':
    main()