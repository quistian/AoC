#!/usr/bin/env python3

import sys

# AoC day one part one

def main():
    tot = 0
    for line in sys.stdin:
        has_digits = False
        line.rstrip()
        lets = list(line)
        for let in lets:
            if let.isdigit():
                tens = int(let)
                has_digits = True
                break
        if has_digits:
            lets.reverse()
            cnt = 0
            for let in lets:
                if let.isdigit():
                    if cnt == 0:
                        ones = int(let)
                    cnt += 1
            if cnt == 1:
                tot += 10*ones + ones
            else:
                tot += 10*tens + ones
    print(tot)

if __name__ == '__main__':
    main()
