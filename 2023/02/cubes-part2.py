#!/usr/bin/env python

import sys

def main():
    tot = 0
    for line in sys.stdin:
        possible = True
        line = line.rstrip()
        toks = line.split(':')
        game_num = int(toks[0].split()[1])
        grabs = toks[1].split(';')
        colmin = { 'red': 1, 'green': 1, 'blue': 1 }
        for grab in grabs:
            selects = grab.split(',')
            for select in selects:
                (num, col) = select.strip().split()
                n = int(num)
                if n > colmin[col]:
                    colmin[col] = n
        power = 1  
        for val in colmin.values():
            power *= val
        print(colmin, power)
        tot += power
    print(tot)

if __name__ == '__main__':
    main()
