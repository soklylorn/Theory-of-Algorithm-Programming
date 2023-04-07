
class Grammar:
    """
    Class representing a CF grammar.
    """

    def __init__(self, start_variable):
        """
        Initialize a Grammar object.

        :param start_variable: The start variable, one of the non-terminals.
        """

        if not non_terminal(start_variable):
            raise ValueError("The start variable must not be terminal")

        self._start_variable = start_variable
        # TODO Initialize the data structure which contains the rules

    def add_rule(self, left, right):
        """
        Add a new derivation rule to the grammar.

        :param left: the left side of the rule, a non terminal symbol
        :param right: string of terminal and non terminal symbols
                      or a list of such strings
        """

        if not non_terminal(left):
            raise ValueError("The left side must be non terminal")

        # TODO Add the rule to the grammar.

    def derive(self, word):
        """
        Search a left-derivation to the given word.

        :param word: a word to derive
        :return: list of derivation steps or `False` if 
                 there is no derivation
        """

        if not word.islower():
            raise ValueError("The word to derivate must not contain non terminal!")

        return self._bfs_search(self._start_variable, word)

    def _bfs_search(self, from_where, to_where):
        """
        Search a path with breadth first search (BFS) algorithm 
        from the vertex `from_where` to the vertex `to_where`. 

        :param from_where: Starting vertex (root in the tree), 
                           a string of terminal and non terminal symbols. 
        :param to_where:   The target vertex, 
                           a string of terminal and non terminal symbols. 
        :return: List of the vertices of the path, or `False`, 
                 if there is no derivation. 
        """
        parent = {}
        seq = [from_where]

        while to_where not in parent:
            if not seq:
                return False
            vertex = seq.pop(0)
            for child in self._next(vertex):
                if child not in parent and child != from_where:
                    parent[child] = vertex
                    seq.append(child)

        return read_path(parent, from_where, to_where)

    def _next(self, vertex):
        """
        Gives the list of end vertices of edges start from `vertex`

        :param vertex: the start vertex, a string of 
                       terminal and non terminal symbols
        :return: the list of derivable strings from `vertex` 
                 by left-derivation steps
        """

        # TODO search for the next words
        return []

def non_terminal(s):
    """
    :param s: the string to exemine
    :return: `True` if `s` is a non terminal symbol
    """

    return len(s) == 1 and s.isupper()

def read_path(parent, from_where, to_where):
    """
    Gives a path from `from_where` to `to_where` in the BFS-tree.

    :param parent: the dictionary of the parents of vertices
    :param from_where: starting vertex of the path
    :param to_where: final vertex of the path
    :return: list of vertices of the path if it exists,
            and False otherwise
    """

    path = []
    if to_where not in parent:
        return path
    vertex = to_where

    while vertex != from_where:
        path.append(vertex)
        vertex = parent[vertex]

    path.append(from_where)
    path.reverse()
    return path

if __name__ == '__main__':
    import sys

    g = Grammar("S")
    g.add_rule("S", ["XSX", "R"])
    g.add_rule("R", ["aTb", "bTa"])
    g.add_rule("T", ["XTX", "X", ""])
    g.add_rule("X", "a")
    g.add_rule("X", "b")

    derivation = g.derive(sys.argv[1])
    if derivation:
        print(" => ".join(derivation))
    else:
        print("No derivation")