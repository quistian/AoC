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

OutCome = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

Value = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3
}

Win = {
        'Rock': 'Paper',
        'Paper': 'Scissors',
        'Scissors': 'Rock'
}

Lose = {}

def main():
    tot = 0
    for a,b in Win.items():
        Lose[b] = a
    for line in sys.stdin:
        (a, b) = line.rstrip().split(' ')
        tot += winnings(a,b)
    print(tot)

def winnings(them, us):
    foe = Opp[them]
    out = OutCome[us]
    if out == 'Draw':
        return 3 + Value[foe]
    if out == 'Win':
        return 6 + Value[Win[foe]]
    else:
        return Value[Lose[foe]]
            
if __name__ == '__main__':
    main()
