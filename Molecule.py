
#############################################################################################

# With a data type for molecular formulae implemented, it is time
# to look at molecules themselves.
#
# Now, a molecule is a labeled, undirected graph, where we use integers to
# identify nodes and `Atom`s as their labels. In addition, we
# need to keep track of the neighbors of atoms, plus the
# types of bonds connecting atoms with their neighbors.
#
# We use a simple integer to describe the bond type: 1 for a single
# bond, 2 for a double bond, and 3 for a triple bond.
#
# A molecule can then be viewed as a dictionary linking nodes (integers)
# to pairs consisting of their labels (`Atom`s) and neighbors
# (dictionaries pairing nodes (integers) with bond types (integers)).
#
# As an example, here is ethanol in such a representation:
#
# ```
#   ethanol = { 0: (Atom("C",3), {1:1}),
#               1: (Atom("C",2), {0:1,2:1}),
#               2: (Atom("O",1), {1:1})
#             }
# ```
#
# As you can see, each of the heavy atoms of ethanol has its own node, while
# we keep the hydrogens implicit (if possible). For every node, we give its
# list of neighbors plus the bond order: For instance, atom 2 (the oxygen)
# is bound via a single bond to atom 1 (the central carbon), which itself
# has two neighbors (0 and 2, both bound via single bonds).
#
# a) Define a new class called `Molecule` that encapsulates the representation
#    above in a field called `mol`.

from Atom import Atom, info
from Formula import Formula, atomicNumber

class Molecule:
    def __init__(self, atoms, edges):
        self.mol = {}
        self.atom = atoms
        self.edges = edges
        for i in range(len(atoms)):
            self.mol[i] = (atoms[i], {})
        for edge in edges:
            self.mol[edge[0]][1][edge[1]] = edge[2]
            self.mol[edge[1]][1][edge[0]] = edge[2]

    def __str__(self):
        return str(self.mol)

    def __repr__(self):
        return str(self.mol)

    def order(self):
        return len(self.mol)

    def size(self):
        size = 0
        for atom in self.mol:
            size += len(self.mol[atom][1])
        return size/2

    def degree(self, node):
        return len(self.mol[node][1])

    def isIsolate(self, node):
        return self.degree(node) == 0

    def isTerminal(self, node):
        return self.degree(node) == 1

    def mass(self):
        return sum([atom.mass() for atom, _ in self.mol.values()])

    def exactMass(self):
        return sum([atom.exactMass() for atom, _ in self.mol.values()])

    def formula(self):
        formula_dict = {}  # Initialize an empty dictionary for the formula
        for atom in self.atom:
            element = atomicNumber(atom.element)  # Convert the element to an atomic number
            # Add the atom to the formula
            if element in formula_dict:
                formula_dict[element] += 1
            else:
                formula_dict[element] = 1
            # Add the hydrogen atoms to the formula
            hydrogens = atom.hydrogens
            if 1 in formula_dict:
                formula_dict[1] += hydrogens
            else:
                formula_dict[1] = hydrogens
        formula = Formula(formula_dict)  # Create a Formula object from the dictionary
        return str(formula)  # Return the formula as a string  # Return the formula as a string

    def hasElement(self, element):
        for atom, _ in self.mol.values():
            if atom.hasElement(element):
                return True
        return False

    def isElement(self, element):
        for atom, _ in self.mol.values():
            if atom.isElement(element):
                return True
        return False

    def isSubstructure(self, other):
        if isinstance(other, Molecule):
            other = other.mol
        for node, (atom, _) in self.mol.items():
            if atom != other[node][0]:
                return False
            for neighbor, bond in other[node][1].items():
                if neighbor not in self.mol[node][1] or self.mol[node][1][neighbor] != bond:
                    return False
        return True

    def isSubgraph(self, other):
        if isinstance(other, Molecule):
            other = other.mol
        for node, (atom, _) in self.mol.items():
            if atom != other[node][0]:
                return False
            for neighbor, bond in other[node][1].items():
                if neighbor not in self.mol[node][1] or self.mol[node][1][neighbor] != bond:
                    return False
        return True
    
#    b) Define a constructor for molecules that takes a list of
#    atoms (the node labels) plus a list of edges (triples consisting
#    of the two nodes plus the bond order), and transforms these
#    into the representation given above. Node, assume that the list of
#    edges contains every edge only once!
#
#    Make sure that this works correctly by creating some molecules and verifying
#    their inner representation.
#
#    Here's an example:
#
#    ```
#    test = Molecule([Atom("C",3),Atom("C",2),Atom("O",1)],[(0,1,1),(1,2,1)])
#    ```
#
#    If you run `print test.mol`, you should see output similar to this:
#
#    ```
#    {0: (<Atom.Atom object at 0x7f619772a2d0>, {1: 1}),
#     1: (<Atom.Atom object at 0x7f619772a350>, {0: 1, 2: 1}),
#     2: (<Atom.Atom object at 0x7f619772a390>, {1: 1})}
#    ```
#
#    Note: There is a more complex example of a molecule commented-out at the
#    end of this source file. Feel free to use it to the functions you are
#    going to implement now.

test = Molecule([Atom("C",3),Atom("C",2),Atom("O",1)],[(0,1,1),(1,2,1)])
# print(test.mol)

# c) The "order" of a graph is the number of nodes it has. Add function
#    `order` to your `Molecule` class and implement it accordingly.

# print(test.order())

# d) The "size" of a graph is the number of edges it has. Add function
#    `edge` to your `Molecule` class and implement it accordingly.
#    Atention: Make sure you count every edge only once even though
#    edges appear twice in a molecule's adjacency representation.

# print(test.size())

# e) The "degree of a node" describes the number of neighbors it has.
#    Add a function `degree` to class `Molecule`
#    that returns the degree of its node input (given as an integer).

# print(test.degree(1))

# f) A node in a graph is "isolate" if it has degree 0. Implement
#    a function `isIsolate` that returns `true` if the node has no neighbors.

# print(test.isIsolate(1))

# g) A node in a graph is "terminal" if it has degree 1. Implement
#    a function `isTerminal` that returns `true` if the node has no neighbors.

# print(test.isTerminal(0))

#
# h) Implement functions `mass` and `exactMass` to compute the molar mass
#    (and exact molar mass) of a molecule.

# print(test.mass())
# print(test.exactMass())

#
# i) Implement function `formula` that computes and returns the
#    molecular formula of a molecule.

# print(test.formula())

#
# j) (hard) You are now going to implement your first graph traversal
#    algorithm.
#
#    A "walk" in a graph is a sequence of nodes, so that every node
#    in the sequence is a neighbor of the previous node in the sequence.
#    For instance, [0,1,2,1] is a walk in ethanol:
#    Atom 0 is a neighbor of atom 1, 1 is a neighbor of 2, and 2
#    is a neighbor of 1. However, [0,1,2,0] is not a walk, since
#    0 is not a neighbor of 2.
#
#    A "trail" is a walk in which no edge is traversed more than once.
#    A "path" is a walk in which no node is visited more than once.
#    If there is a path from node `u` to `v`, the two nodes are said
#    to be "connected". Every node is trivially connected to itself.
#
#    Given a molecule and two of its nodes, write a function that
#    determines if the two nodes are connected.

def isPath(molecule, node1, node2, visited=None):
    if visited is None:
        visited = []
    if node1 == node2:
        return True
    if node1 in visited:
        return False
    visited.append(node1)
    for neighbor in molecule.mol[node1][1]:
        if isPath(molecule, neighbor, node2, visited):
            return True
    return False

# print(isPath(test, 0, 2))

#
# k) (hard) As in part j), we are going to look for a path between
#    nodes. This time, however, you should implement function
#    `findPath` that tries to find a path between two nodes in a
#    molecule. The function should return a list of the node indices
#    in the path in the correct order. If the two nodes are not
#    connected, the empty list should be returned.

def findPath(molecule, node1, node2, visited=None):
    if visited is None:
        visited = []
    if node1 == node2:
        return [node1]
    if node1 in visited:
        return []
    visited.append(node1)
    for neighbor in molecule.mol[node1][1]:
        path = findPath(molecule, neighbor, node2, visited)
        if path:
            return [node1] + path
    return []


print(findPath(test, 0, 2))

#
# l) Even if you haven't finished everything, you might want to test
#    your code with the following non-trivial molecule (tyrosine
#    hydro chloride).
#
#
# ```
tyrosineHCl = Molecule([ Atom("N",3,1),   #0
                        Atom("C",1),     #1
                        Atom("C"),       #2
                        Atom("O"),       #3
                        Atom("O",1),     #4
                        Atom("C",2),     #5
                        Atom("C"),       #6
                        Atom("C",1),     #7
                        Atom("C",1),     #8
                        Atom("C"),       #9
                        Atom("C",1),     #10
                        Atom("C",1),     #11
                        Atom("O",1),     #12
                        Atom("Cl",0,-1)],#13
                        [ (0,1,1),
                        (1,2,1),
                        (1,5,1),
                        (2,3,2),
                        (2,4,1),
                        (5,6,1),
                        (6,7,1),
                        (6,11,2),
                        (7,8,2),
                        (8,9,1),
                        (9,10,2),
                        (9,12,1),
                        (10,11,1) ]
                        )
# ```
#    Its order is 14.
#    Its size is 13.
#    Its mass is 217.694.
#    Its exact mass is 217.050570924.
#    Its formula is C9H12ClNO3.
#    Its terminal nodes are nodes 0, 3, 4, and 12.
#    It hase only once isolte node: Node 13.
#    Node 13 is connected to no other node (it is isolate after all),
#    but all other nodes are connected.

print(tyrosineHCl.order())
print(tyrosineHCl.size())
print(tyrosineHCl.mass())
print(tyrosineHCl.exactMass())
print(tyrosineHCl.formula())
print(tyrosineHCl.isTerminal(0))
print(tyrosineHCl.isTerminal(3))
print(tyrosineHCl.isTerminal(4))
print(tyrosineHCl.isTerminal(12))
print(tyrosineHCl.isIsolate(13))
print(tyrosineHCl.isIsolate(0))
print(findPath(tyrosineHCl, 0, 13))