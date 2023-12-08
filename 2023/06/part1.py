#!/usr/bin/env python

import sys

def main():
    prod = 1
    for line in sys.stdin:
        toks = line.split()
        if toks[0] == 'Time:':
            tau = toks[1:]
        if toks[0] == 'Distance:':
            dist = toks[1:]
    for t,d in zip(tau, dist):
        prod *= quad(int(t), int(d))
    print(prod)

# the time distance button boat game resolves to the quadratic:
# d = t * V = t * (T - t) etc.
# t^2 -Tt + d < 0   T total time  D record distance

def quad(T, d):
    cnt = 0
    for t in range(1,T):
        if (t*t - T*t + d) < 0:
            cnt += 1
    return cnt

if __name__ == '__main__':
    main()
