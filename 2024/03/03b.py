#!/usr/bin/env python3

import re
import sys
from pathlib import Path

def first_chunk(mangled):
    target = r'(.*)don\'t\(\)'
    m = re.match(target, mangled)
    fnd = m.group(1)
    print(fnd)
    print(m.span())
    return fnd

def do_muls(sstr):
    sum = 0
    target = r'mul\((\d+),(\d+)\)'
    for m in re.finditer(target, sstr):
        sum += int(m.group(1)) * int(m.group(2))
    return sum

def do_areas(sstr):
    sum = 0
    do_target - r'do\(\)(.*)don\'t\(\)'

def dont_areas(sstr):
    sum = 0
    dont_do_target = r'don\'t\(\)(.+?)do\(\)'
    for m in re.finditer(dont_do_target, sstr, flags=re.DOTALL):
        sum += do_muls(m.group(1))
        (b,e) = m.span()
    do_idx = e
    print('dont-do sum', sum)
    dont_target = r'don\'t\(\)'
    for m in re.finditer(dont_target, sstr):
        (b,e) = m.span()
        if b > do_idx:
            dont_idx = e
            break
    if b > do_idx:
        sum += do_muls(sstr[dont_idx:])
    return sum

def main():
    """ AoC 2024 Day 1 Part a. """
    sum1 = 0
    sum2 = 0
    inf = "03.input"
    f = Path(inf)
    if f.exists() and f.is_file():
        with f.open() as fd:
            instr = fd.read()
    sum1 = do_muls(instr)
    print('all sums:', sum1)
    sum2 = dont_areas(instr)
    print('dont area sums:', sum2)
    print('sums only in do areas:', sum1 - sum2)
    exit()
    dont_chunks = re.findall(dont_target, instr)
    print('num of dont chunks', len(dont_chunks))
    for chunk in dont_chunks:
        ll = re.findall(mul_target, chunk)
        for duo in ll:
            (i, j) = duo
            sum2 += int(i) * int(j)
    print(sum2)
    print(sum1 - sum2)
        

if __name__ == '__main__':
    main()