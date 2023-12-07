# In this module, you are going to implement a data type (class)
# plus several utility functions for working with molecular formulae.
#
# Internally, a molecular formula is a mapping (dictionary) from
# atomic number to the count of the element in question.
# You are not only going to implement a
# parser and pretty printer for molecular formulae but also some
# utility functions for comparing molecular formulae, which is
# extremely useful and efficient in substructure searches.
#
# Before you implement the actual `Formula` class, your are first
# going to define and implement a bunch of utility functions.
#
# Just a small hint: All utility functions we implement are here for
# a reason. Make use of them!
#
# Let's get started.

from Data import info
from Atom import fromSymbol

# a) Implement a function `symbol`, which returns the element
#    symbol of its argument: If the argument is an `int`, it should
#    be treated as an atomic number and converted, else it should be treated
#    as an element symbol and returned.

def symbol(element):
    return info[element]['symbol'] if isinstance(element, int) else fromSymbol[element]

#
# b) Implement a function `atomicNumber`, which returns the atomic
#    number of its argument: If the argument is an `int`, it should
#    be treated as an atomic number and returned, else it should be treated
#    as an element symbol and converted.

def atomicNumber(element):  
    return element if isinstance(element, int) else fromSymbol[element]

# c) Implement a function `addElement` taking three arguments:
#
#      * the first argument called `formula` should be a dictionary
#        mapping atomic numbers to counts
#
#      * the second argument called `element` should be an element
#        symbol or atomic number
#
#      * the third argument called `count` should be the number
#        of atoms of the given element we want to insert
#
#    The function should behave as follows: If the count is negative,
#    do nothing, else if the element is already in the dictionary,
#    add the count to the count in the dictionary, else insert
#    the element plus its count into the dictionary. Make sure
#    to convert `element` to an atomic number first!

def addElement(formula, element, count):
    if count < 0:
        return
    element = atomicNumber(element)
    if element in formula:
        formula[element] += count
    else:
        formula[element] = count

#
# d) Implement a function `formulaFromList`, which takes a list of
#    element-count pairs and inserts them into a dictionary.
#    Elements in the list can be given either as element symbols or
#    as atomic numbers.
#
#    Note: The function should behave correctly even if the
#    list has double entries. For instance:
#    
#      formulaFromList([("C",1),("H",3),("C",1),("H",2),("O",1),("H",1)])
#      >>> {6: 2, 1: 6, 8: 1}
#      formulaFromList([(6,1),(1,3),(6,1),(1,2),(8,1),(1,1)])
#      >>> {6: 2, 1: 6, 8: 1}

def formulaFromList(pairs):
    formula = {}
    for element, count in pairs:
        addElement(formula, element, count)
    return formula

#
# e) Implement a function `parseFormula`, which should read a formula
#    as a string and convert it to a dictionary of atomic number-count
#    pairs. The result should be able to correctly parse and convert
#    the following examples:
#
#      "C2H6O"
#      "CH3CH2OH"
#      "HCCl3"
#      "H1C1C0Cl3"
#
#    While this can be a bit of a pain to implement, it will be tremendously
#    useful, when we want to quickly come up with a molecular formula for
#    testing.

def element(pos, string):
    if pos < len(string)-1 and string[pos+1].islower():
        return pos+2, atomicNumber(string[pos:pos+2])
    elif string[pos].isupper():
        return pos+1, atomicNumber(string[pos])
    else:
        return pos, 0


def counter(pos, string):
    count = 0
    i = 0
    while pos + i < len(string)-1:
        # if string[pos + i].isalpha() and string[pos+i+1].isalpha():
        #     return pos + i, 1
        if string[pos + i].isdigit():
            count = count * 10 + int(string[pos + i])
            i += 1
        else:
            break
    return pos + i, max(1, count)


    
def parseFormula(string):
    formula = {}
    pos = 0
    while pos < len(string):
        pos, elem = element(pos, string)
        if elem == 0:
            break
        pos, count = counter(pos, string)
        addElement(formula, elem, count)
    return formula


# g) Implement a function `numAtoms(formula,element)` for extracting the number of atoms
#    stored in the given formula for the given element (as a symbol or atomic number).
#    This should return `0` if the element in question is not present in the
#    dictionary.

def numAtoms(formula, element):
    return formula[atomicNumber(element)] if atomicNumber(element) in formula else 0


#
# h) Implement function `printPair(element,count)` which should return a
#    string representing the given element-count pair. As usual, the element
#    can be given as a symbol or atomic number.
#
#    Example:
#      printPair('C',2)
#      >>> 'C2'
#      printPair('Cl',1)
#      >>> 'Cl'
#      printPair('O',0)
#      >>> ''
#      printPair(6,3)
#      >>> 'C3'

def printPair(element, count):
    element = atomicNumber(element)
    if count == 1:
        return symbol(element)
    elif count == 0:
        return ''
    else:
        return symbol(element) + str(count)
    
#
# i) Implement a function `printFormula` for pretty printing
#    molecular formulae in Hill order. Make sure to correctly sort
#    everything before assembling the string, and use `printPair`
#    in your implementation.
def printFormula(formula):
    formula = {symbol(number): count for number, count in formula.items()}
    result = ''
    if 'C' in formula:
        result += printPair('C', formula['C'])
        del formula['C']
    if 'H' in formula:
        result += printPair('H', formula['H'])
        del formula['H']
    for element in sorted(formula.keys()):
        result += printPair(element, formula[element])
    return result


#
# j) It is now time to assemble all these utilities in a class
#    called `Formula`. The class constructor `__init__` should
#    take a single argument of type `list`, `dict`, or `str` and
#    use it to correctly generate an internal field `self.__formula`,
#    which is a dictionary mapping atomic numbers to counts.
#    All functionality needed to do this has already been implemented.
#
#    The class should also have a `__str__` function for proper pretty
#    printing. Here's an example session:
#
#    print(Formula("CH3CH2OH")
#    >>> C2H6O

class Formula:
    def __init__(self, formula):
        self.__formula = parseFormula(formula) if isinstance(formula, str) else formula
    def __str__(self):
        return printFormula(self.__formula)
    def __repr__(self):
        return str(self.__formula)
    def __getitem__(self, element):
        return self.__formula[atomicNumber(element)] if atomicNumber(element) in self.__formula else 0
    def __contains__(self, element):
        return atomicNumber(element) in self.__formula
    def __add__(self, other):
        if isinstance(other, Formula):
            other = other.__formula
        result = self.__formula.copy()
        for element, count in other.items():
            addElement(result, element, count)
        return Formula(result)
    def __sub__(self, other):
        if isinstance(other, Formula):
            other = other.__formula
        result = self.__formula.copy()
        for element, count in other.items():
            addElement(result, element, -count)
        return Formula(result)
    def __eq__(self, other):
        if isinstance(other, Formula):
            other = other.__formula
        return self.__formula == other
    def __ne__(self, other):
        if isinstance(other, Formula):
            other = other.__formula
        return self.__formula != other
    def mass(self):
        return sum([info[number]['mass'] * count for number, count in self.__formula.items()])
    def exactMass(self):
        return sum([info[number]['exactMass'] * count for number, count in self.__formula.items()])
    def numAtoms(self, element):
        return self.__formula[atomicNumber(element)] if atomicNumber(element) in self.__formula else 0
    def hasElement(self, element):
        return atomicNumber(element) in self.__formula
    def containsFormula(self, other):
        other = parseFormula(other)
        for element, count in other.items():
            if element not in self.__formula or self.__formula[element] < count:
                return False
        return True
    def addFormula(self, other):
        if isinstance(other, str):
            other = parseFormula(other)
        for element, count in other.items():
            addElement(self.__formula, element, count)
        return self
    


# k) Implement functions `mass` and `exactMass` on `Formula`. It should
#    be obvious from their name, what they return.

# Done directly in the implementation of the class

#
# l) Implement functions `numAtoms` and `hasElement` on `Formula`.
#    They should take a single element (symbol or atomic number) as input
#    and each return the obvious result.

# Done directly in the implementation of the class

#
# m) Implement function `containsFormula` on `Formula`: It should take
#    another formula (as a list of pairs, a dictionary, a Formula, or a string)
#    and check if it contains every element in its argument in at least
#    the given count.
#
#    This function is a very efficient pre-filter in substructure searches:
#    If we want to check if a molecule A contains molecule B as a
#    substructure, we can quickly check if the formula of A contains the
#    formula of B. If that is not the case, B can impossibly be a substructure
#    of A, and we can move on without having to do a proper substructure
#    search.

# Done directly in the implementation of the class

#
# n) Implement function `addFormula` on `Formula`: It should take
#    another formula (as a list of pairs, dictionary, Formula, or string)
#    as input and insert it in the obvious into the current formula.

# Done directly in the implementation of the class

