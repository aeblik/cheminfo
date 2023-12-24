# Exercise:
#
#   a) Using dictionary `info` in `Data.py`, create a second dictionary
#      `fromSymbol` in the same module for converting the symbol of an element
#      to the corresponding atomic number
from Data import info
fromSymbol = {element['symbol']: index for index, element in enumerate(info)}
# print(fromSymbol)



#   b) Define a simple class for holding the following information of an atom
#      as instance variables:
#     * Element (given as the atomic number)
#     * Number of implicit hydrogens
#     * Charge
#      Make sure that the constructor of the class can be called with
#      the following syntax:
#        Atom(6,0,0)
#        Atom(6,1,0)
#        Atom(6,2,0)
#        Atom(6,0,1)
#        Atom(6,0,2)
#        Atom(6,0,-1)
#        Atom(6,0,-2)
#        Atom(6,2,1)
#      The constructor should raise an exception if the arguments are
#      invalid, e.g. if the atomic number is not a positive integer.
#      The constructor should also raise an exception if the sum of
#      implicit hydrogens and charge is greater than 4.
class Atom:
    '''
    This class represents an atom in a molecule.

    Attributes:
    element (int): The atomic number of the atom.
    hydrogens (int): The number of hydrogen atoms bonded to this atom. Default is 0.
    charge (int): The charge of the atom. Default is 0.

    Raises:
    ValueError: If the atomic number is less than 1.
    ValueError: If the sum of the number of hydrogen atoms and the charge is greater than 4.
    '''
    def __init__(self, element, hydrogens=0, charge=0):
        if element < 1:
            raise ValueError('Atomic number must be a positive integer')
        if hydrogens + charge > 4:
            raise ValueError('Sum of implicit hydrogens and charge must be <= 4')
        self.element = element
        self.hydrogens = hydrogens
        self.charge = charge

#   c) For class `Atom`, define a function `symbol` that returns the symbol
#      corresponding to the atom's element.


def symbol(self):
    '''
    Returns the symbol of the atom's element.

    '''
    return info[self.element]['symbol']
Atom.symbol = symbol

#   d) For class `Atom`, define a function `mass` that returns the atom's
#      atomic mass. Make sure to include the mass from implicit hydrogen
#      atoms. Do the same thing for `exactMass`.
def mass(self):
    '''
    Returns the mass of the atom.
    '''
    return info[self.element]['mass'] + self.hydrogens * info[1]['mass']
Atom.mass = mass
def exactMass(self):
    return info[self.element]['exactMass'] + self.hydrogens * info[1]['exactMass']
Atom.exactMass = exactMass
#
#   e) For class `Atom`, define a `__str__` function for pretty printing
#      the atom: The symbol followed by an `H` and the number of implicit
#      hydrogens (if any), followed by the charge (if any).
#      Example output:
#        print(Atom(6,0,0))
#        >>> C
#        print(Atom(6,1,0))
#        >>> CH
#        print(Atom(6,2,0))
#        >>> CH2
#        print(Atom(6,0,1))
#        >>> C+
#        print(Atom(6,0,2))
#        >>> C+2
#        print(Atom(6,0,-1))
#        >>> C-
#        print(Atom(6,0,-2))
#        >>> C-2
#        print(Atom(6,2,1))
#        >>> CH2+
def __str__(self):
    '''
    Returns a string representation of the atom.
    '''
    return self.symbol() + ('H'+ str(self.hydrogens) if self.hydrogens >0 else '') + str(self.charge if self.charge not in(0, 1) else '') + ('+' if self.charge > 0 else '')
Atom.__str__ = __str__

#   f) Refine the constructor of class `Atom` in such a way that arguments
#      `hydrogens` and `charge` are optional, i.e. that it's possible to create
#      an `Atom` just by writing `Atom(6)`.
#      This was done in the first place already.


#   g) Refine the constructor of class `Atom` in such a way that
#      instead of the atomic number, we can also provide an element symbol.
#      You need to perform some runtime type checking for this to work.
def __init__(self, element, hydrogens=0, charge=0):
    '''
    Initializes an Atom object.
    '''
    if isinstance(element, str):
        element = fromSymbol[element]
    if element < 1:
        raise ValueError('Atomic number must be a positive integer')
    if hydrogens + charge > 4:
        raise ValueError('Sum of implicit hydrogens and charge must be <= 4')
    self.element = element
    self.hydrogens = hydrogens
    self.charge = charge
Atom.__init__ = __init__

