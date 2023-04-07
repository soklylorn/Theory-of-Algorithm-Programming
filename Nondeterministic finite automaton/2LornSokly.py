"""I encoded this program myself, did not copy or rewrite the code of others,and did not give or send it to anyone else. Lorn Sokly"""


#!/usr/bin/env python3

# START

q0 = 0 # initial state

f = {2,5,6} # accept states 

def delta(q, a):
    
    if q == 0:       
        if a == 'a':
            return {1}
        elif a== " ":
            return {6}
        else:
            return {0}
        
    elif q == 1:
        if a == 'a':
            return {2}
        elif a== 'l':
            return {3}
        else:
            return {1}
        
    elif q == 2:
        if a == 'a':
            return {3}
        elif a == 'l':
            return {3}
        else:
            return {2}
        
    elif q == 3:
        if a == 'g':
            return {4}
        elif a == 'a':
            return {2}
        else:
            return {3}
        
    elif q == 4:
        if a=='a':
            return {2}
        elif a == 'p':
            return {5}
        else:
            return {4}
    elif q == 5:
        if a == 'a':
            return {6}
        else:
            return {5}
    elif q == 6:
        return {6,2}

# END

def recognize(word):
    qs = set([q0])
    for a in word:
        qs_prime = set()
        for q in qs:
            qs_prime.update(delta(q, a))
        qs = qs_prime
    return f.intersection(qs) # check if the machine accept the languages/words

def main(args):
    word = args[1]
    if recognize(word):  # if TRUE = after the final character of the words ends up in one of the accept states. 
        print('word accepted')
    else:       # otherwise
        print('word NOT accepted')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))