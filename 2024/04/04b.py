#!/usr/bin/env python3

import re
import sys
from pathlib import Path
# from rich import print

import numpy as np

def cnt_non_overlapping(target, sstr):
    return len(re.findall(target, sstr))

def cnt_fwd_rev(target, sstr):
    return cnt_non_overlapping(target, sstr) + cnt_non_overlapping(target, sstr[::-1])


def get_column(idx, array):
    colstr = ""
    for row in range(len(array[0])):
        colstr += array[row][idx]
    return colstr


def main():
    """ AoC 2024 Day 4 Part b. """
    inf = "04.input"
    word = 'XMAS'
    matrix = []
    lines = []
    cnt = 0
    f = Path(inf)
    if f.exists() and f.is_file():
        with f.open() as fd:
            lls = fd.readlines()
            for ll in lls:
                l = ll.strip()
                lines.append(l)
                matrix.append(list(l))
    a = np.array(matrix)
    b = np.fliplr(a)
    (h, w) = a.shape
    for l in lines: # cnt the XMAS strings in the rows
        cnt += cnt_fwd_rev(word, l)
    for r in range(h): # cnt the XMAS strings in the columns
        col = ''.join(a[0:,r])
        cnt += cnt_fwd_rev(word, col)
    diag = ''.join(a.diagonal()) # main diagonals
    cnt += cnt_fwd_rev(word, diag)
    diag = ''.join(b.diagonal()) # main diagonals
    cnt += cnt_fwd_rev(word, diag)
    for o in range(1, w - len(word) + 1): # both diagonals
        diag = ''.join(a.diagonal(o)) # upper diagonal
        cnt += cnt_fwd_rev(word, diag)
        diag = ''.join(a.diagonal(-o)) # lower diagonal
        cnt += cnt_fwd_rev(word, diag)
        diag = ''.join(b.diagonal(o)) # upper diagonal
        cnt += cnt_fwd_rev(word, diag)
        diag = ''.join(b.diagonal(-o)) # lower diagonal
        cnt += cnt_fwd_rev(word, diag)
    print('row,col,upper diag',cnt)

    

    exit()

if __name__ == '__main__':
    main()
