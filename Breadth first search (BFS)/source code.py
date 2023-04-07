
def read_graph(f):
    """
    Read a graph from a text file.

    :param f: the file to read
    :return: the edge-list, the starting and final vertex of path
    """

    header = f.readline().split()
    n, m, from_where, to_where = [int(s) for s in header]

    graph = dict((i, []) for i in range(n))
    for j in range(m):
        edge = f.readline().split()
        u, v = [int(s) for s in edge]
        graph[u].append(v)

    return graph, from_where, to_where

def search_path(graph, from_where, to_where):
    """
    Search a shortest path between the two vertices.

    :param graph: the edge-list of the graph
    :param from_where: starting vertex of the path
    :param to_where: final vertex of the path
    :return: a list of vertices of the shortest path if it exists, 
             and False otherwise
    """

    # TODO the place to write the breadth first search (BFS) algorithm

    return read_path({}, from_where, to_where)

def read_path(parent, from_where, to_where):
    """
    Gives a path from from_where to to_where vertex in the BFS-tree

    :param parent: the dictionary of the parents of a vertex
    :param from_where: starting vertex of the path
    :param to_where: final vertex of the path
    :return: list of vertices of the path if it exists, 
             and False otherwise
    """

    if to_where not in parent:
        return False

    path = []
    vertex = to_where

    while vertex != from_where:
        path.append(vertex)
        vertex = parent[vertex]

    path.append(from_where)
    path.reverse()
    return path

if __name__ == '__main__':

    import sys

    with open(sys.argv[1], 'r') as f:
        graph, from_where, to_where = read_graph(f)
    path = search_path(graph, from_where, to_where)

    if path:
        print('path: ' + ' -> '.join(str(i) for i in path))
    else:
        print('no path')