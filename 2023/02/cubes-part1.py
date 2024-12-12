#!/usr/bin/env python

import sys

def main():
    colmax = {
            'red': 12,
            'green': 13,
            'blue': 14
    }
    tot = 0
    for line in sys.stdin:
        possible = True
        line = line.rstrip()
        toks = line.split(':')
        game_num = int(toks[0].split()[1])
        grabs = toks[1].split(';')
        for grab in grabs:
            selects = grab.split(',')
            for select in selects:
                (num, col) = select.strip().split()
                if int(num) > colmax[col]:
                    possible = False
        if possible:
            tot += game_num
    print(tot)

if __name__ == '__main__':
    main()
