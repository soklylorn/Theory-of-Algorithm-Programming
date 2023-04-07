"""I encoded this program myself, did not copy or rewrite the code of others,and did not give or send it to anyone else. Lorn Sokly"""


import sys

def read_graph(filename):  # from previous 3rd task
    with open(filename) as f:
        # read the number of vertices n and edges m
        n, m = map(int, f.readline().split()) # read the first line by readline()
        # map(int, ...) applies the int function to each element of the resulting list

        # initialize an empty graph with n vertices
        graph = {i: set() for i in range(n)}

        # read each edge and add it to the graph
        for _ in range(m):
            u, v = map(int, f.readline().split())
            # add edge to both endpoints since graph is non directed 
            graph[u].add(v)
            graph[v].add(u)

    return graph

def hamiltonian_cycle(graph, seq):
    # check if cycle has the correct length
    n = len(graph)
    if len(seq) != n:
        return False

    # check if each vertex occurs exactly once
    if len(set(seq)) != n:  # set(seq) here will list all the vertices exactly once in the form of a dictionary
        return False

    # check if there are edges between each pair of consecutive vertices
    for i in range(n):
        u, v = seq[i], seq[(i+1)%n] #(i+1)%n = remainder of (i+1)/n  loop back to the first vertex if we have reached the end of the sequence
        if v not in graph[u]:
            return False

    return True

if __name__ == '__main__':
    # read the graph from file
    graph = read_graph(sys.argv[1])

    # read the sequence of numbers from file
    with open(sys.argv[2]) as f:
        seq = list(map(int, f.readline().split()))

    # check if the sequence of numbers represents a Hamiltonian cycle in the graph
    if hamiltonian_cycle(graph, seq):
        print('Hamiltonian cycle')
    else:
        print('Not a Hamiltonian cycle')
