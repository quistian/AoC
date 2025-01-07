#!/usr/bin/env python3

import re
import sys
from pathlib import Path
# from rich import print

import numpy as np

def get_square(m,r,c):
    return(m[r:r+3, c:c+3])

def get_diag(m):
    return "".join([m[0,0], m[1,1], m[2,2]])

def get_anti_diag(m):
    return "".join([m[2,0], m[1,1], m[0,2]])

def is_x_mas(m):
    diag = get_diag(m)
    anti = get_anti_diag(m)
    if diag == 'MAS':
        if anti == 'SAM' or anti == 'MAS':
            return True
    elif diag == 'SAM':
        if anti == 'MAS' or anti == 'SAM':
            return True
    return False

def main():
    """ AoC 2024 Day 4 Part b. """
    inf = "04.input"
    matrix = []
    cnt = 0
    f = Path(inf)
    if f.exists() and f.is_file():
        with f.open() as fd:
            lls = fd.readlines()
            for ll in lls:
                l = ll.strip()
                matrix.append(list(l))
    a = np.array(matrix)
    (h, w) = a.shape
    for r in range(0,h-2):
        for c in range(0,w-2):
            b = get_square(a,r,c)
            if is_x_mas(b):
                cnt += 1
    print(b,cnt)

if __name__ == '__main__':
    main()
