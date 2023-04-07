#!/usr/bin/env python3

# START

q0 = 0

f = {0, 1, 3}

def delta(q, a):
    if q == 0:
        if a == 'a':
            return {1, 2}
        else:
            return set()
    elif q == 1:
        if a == 'a':
            return {1}
        else:
            return set()
    elif q == 2:
        if a == 'b':
            return {3}
        else:
            return set()
    elif q == 3:
        if a == 'a':
            return {2}
        elif a == 'b':
            return set()
        else:
            return {3}
    else:
        return set()

# END

def recognize(word):
    qs = set([q0])
    for a in word:
        qs_prime = set()
        for q in qs:
            qs_prime.update(delta(q, a))
        qs = qs_prime
    return f.intersection(qs)

def main(args):
    word = args[1]
    if recognize(word):
        print('word accepted')
    else:
        print('word NOT accepted')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))