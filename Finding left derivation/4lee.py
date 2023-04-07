# Finding left derivation
class Grammar:
    """
    Class representing a CF grammar.
    """

    def __init__(self, start_variable):   # the constructor method of the Grammar class
        # takes a single argument, "start_variable", which is the starting variable of the grammar.
        if not non_terminal(start_variable):
                        
            # If start_variable is a terminal symbol, it raises a ValueError
            
            raise ValueError("The start variable must not be terminal")
            
        self._start_variable = start_variable # if not a terminal symbol, sets the starting variable to _start_variable
        self._rules = {}  # Initializes an empty dictionary _rules to store the rules

    def add_rule(self, left, right):  # left is the left-hand side of the production rule, right can be a string or a list of strings

        """This method adds a new production rule to the grammar. It takes two arguments, 
        left and right, representing the left-hand side and right-hand side of the rule"""
        
        if not non_terminal(left):
            # If left is a terminal symbol, it raises a ValueError
            raise ValueError("The left side must be non terminal")

        if isinstance(right, str):  # if right is a string, then convert it to a list of the string
            right = [right]

        if left not in self._rules:  # Check whether the non-terminal symbol represented by the string left already exists as a key in the _rules dictionary
            self._rules[left] = []

        self._rules[left].extend(right) 
        # adds one or more right-hand sides to the list of production rules associated with the non-terminal symbol represented by the string left

    def derive(self, word):

        if not word.islower():
            # If the word is not in lowercase (Capital letters), then raise value Errors
            raise ValueError("The word to derivate must not contain non terminal!")

        return self._bfs_search(self._start_variable, word) 
        # return the path of the searched word through bfs

    def _bfs_search(self, from_where, to_where):  

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