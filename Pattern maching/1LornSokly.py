"""I encoded this program myself, did not copy or rewrite the code of others,and did not give or send it to anyone else. Lorn Sokly"""
import sys
# S = text
# M = pattern
def simple_matching(S, M):
    n = len(S)
    m = len(M)
    comparisons = 0
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            comparisons += 1
            if S[i+j] != M[j]:
                match = False
                break   # break if no matching, then straight to return comparisons, -1
        if match==True:
            return comparisons, i+1 
    return comparisons, -1  # return -1 if no matching

def quick_search(S, M):
    comparisons = 0
    m = len(M)
    n = len(S)
    # create a list U to store the data of how many characters we should skip when mismatch
    U = [m] * 256  # initialize U with m for all the ASCII characters
    for i in range(m-1):
        U[ord(M[i])] = m - i - 1
    k = 0  # shift k
    while k <= n - m:
        i = m - 1
        while i >= 0 and M[i] == S[k+i]:
            i -= 1  #if they match, then move to the previous character in the pattern M
            comparisons += 1
        if i == -1: #if they match (pattern and text) then return...
            return comparisons, k+1  # return the number of comparisons and the position of the 1st occurrence
        k += U[ord(S[k+m-1])]  #  if mismatch, we skip some characters in the text
        comparisons += 1
    return comparisons, -1  # return the number of comparisons and return -1 if there is no matching left

def main():
    filename = sys.argv[1]
    with open(filename,'r') as file:
        S = file.read().strip()
        file.close()
    M = sys.argv[2]
    s_comparison, s_position = simple_matching(S, M)
    q_comparison, q_position = quick_search(S, M)
    if s_position != -1:
        print(f"Simple search: {s_comparison:5d} comparisons, the pattern starts at {s_position:4d}")
    else:
        print(f"Simple search: {s_comparison:5d} comparisons, no pattern")
    if q_position != -1:
        print(f"Quick search:  {q_comparison:5d} comparisons, the pattern starts at {q_position:4d}")
    else:
        print(f"Quick search:  {q_comparison:5d} comparisons, no pattern")
if __name__ == '__main__':
    main()
    