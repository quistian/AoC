#!/usr/bin/env python3

import sys

# AoC day one part two

def main():
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ndigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    tot = 0
    numeric = list()
    for line in sys.stdin:
        line = line.rstrip()
        mini = 10000
        maxi = -1
        for word in digits:
            ldx = line.find(word)
            if ldx != -1:
                if ldx < mini:
                    mini = ldx
                    tens = digits.index(word)
            rdx = line.rfind(word)
            if rdx != -1:
                if rdx > maxi:
                    maxi = rdx
                    ones = digits.index(word)
        for digit in ndigits:
            ldx = line.find(digit)
            if ldx != -1:
                if ldx < mini:
                    mini = ldx
                    tens = ndigits.index(digit)
            rdx = line.rfind(digit)
            if rdx != -1:
                if rdx > maxi:
                    maxi = rdx
                    ones = ndigits.index(digit)
        tot += tens * 10 + ones
    print(tot)

if __name__ == '__main__':
    main()
