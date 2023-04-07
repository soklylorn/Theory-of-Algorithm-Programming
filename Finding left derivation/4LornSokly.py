"""I encoded this program myself, did not copy or rewrite the code of others,and did not give or send it to anyone else. Lorn Sokly"""


class Grammar:

    def __init__(self, start_variable):

        if not non_terminal(start_variable):
            raise ValueError("The start variable must not be terminal")

        self._start_variable = start_variable
        self._rules = {}   # Initializes an empty dictionary _rules to store the rules

    def add_rule(self, left, right):

        if not non_terminal(left):
            raise ValueError("The left side must be non terminal")

        if isinstance(right, str):
            right = [right]  # Convert string to list 

        if left not in self._rules:
            self._rules[left] = []

        self._rules[left].extend(right)

    def derive(self, word):

        if not word.islower():
            raise ValueError("The word to derivate must not contain non terminal!")

        return self._bfs_search(self._start_variable, word)

    def _bfs_search(self, from_where, to_where, max_iteration=100000):
        parent = {}
        seq = [from_where]
        visited = set([from_where]) # keep track of visited nodes
        count = 0
    
        while to_where not in parent and count < max_iteration:
            if not seq:
                return False
            vertex = seq.pop(0)
            for child in self._next(vertex):
                if child not in visited and child != from_where:
                    parent[child] = vertex
                    seq.append(child)
                    visited.add(child) # add child to visited set
            count += 1
    
        if to_where not in parent:
            return False
    
        return read_path(parent, from_where, to_where)

    def _next(self, vertex):

        if not vertex:
            return []

        words = []
        if vertex[0].isupper():
            for rule in self._rules.get(vertex[0], []):
                words.append(rule + vertex[1:])

        for i in range(1, len(vertex)):
            if vertex[i].isupper():
                for rule in self._rules.get(vertex[i], []):
                    words.append(vertex[:i] + rule + vertex[i + 1:])

        return words


def non_terminal(s):

    return len(s) == 1 and s.isupper()


def read_path(parent, from_where, to_where):

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