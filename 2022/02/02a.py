#!/usr/bin/env python

import sys

Opp = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

Me = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

Value = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3
}

def main():
    tot = 0
    for line in sys.stdin:
        (a, b) = line.rstrip().split(' ')
        tot += winnings(a,b)
    print(tot)

def winnings(them, us):
    return rules(Opp[them], Me[us]) + Value[Me[us]]

def rules(them, us):
    if them == us:
        return 3
    if them == 'Paper' and us == 'Scissors':
            return 6
    if them == 'Scissors' and us == 'Rock':
            return 6
    if them == 'Rock' and us == 'Paper':
            return 6
    return 0

if __name__ == '__main__':
    main()
