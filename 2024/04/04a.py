#!/usr/bin/env python3

import re
import sys
from pathlib import Path

import numpy as np

def cnt_overlapping(target, sstr):
    cnt = 0
    idx = 0
    for i in range(len(sstr)):
        i = sstr.find(target, idx)
        if i > 0:
            idx = i + 1
            cnt += 1
        else:
            break
    return cnt

def get_column(idx, array):
    colstr = ""
    for row in range(len(array[0])):
        colstr += array[row][idx]
    return colstr


def main():
    """ AoC 2024 Day 4 Part a. """
    inf = "04.input"
    word = 'XMAS'
    matrix = []
    lines = []
    row = 0
    f = Path(inf)
    if f.exists() and f.is_file():
        with f.open() as fd:
            lls = fd.readlines()
            for ll in lls:
                l = ll.strip()
                lines.append(l)
                matrix.append(list(l))
    for ln in lines:
        print(ln, cnt_overlapping(word,ln))
        revstr = ln[::-1]
        print(revstr, cnt_overlapping(word, revstr))
        print()
    col1 = get_column(0, matrix)
    print(col1, cnt_overlapping(word, col1))
    revstr = col1[::-1]
    print(revstr, cnt_overlapping(word, revstr))

    exit()

if __name__ == '__main__':
    main()