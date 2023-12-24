from Formula import Formula
'''
This a testing file for the Formula class.
It reads a file with formulas and calculates the heaviest, lightest, most atoms, least atoms, average mass and average number of C-atoms.
It prints the formula and the mass of said formulas.
To run the test file please update the file path to the correct path on your computer.
'''

file_path = r"C:\Daten\ChemInfo\datalab23\Exercises\hs23_datalab_formulae.txt"
with open(file_path, "r") as file:
    f = file.read()

molecules = f.split('\n')

# find the heaviest molecule and print the mass and the formula
heaviest = Formula(molecules[0])
for molecule in molecules:
    if Formula(molecule).mass() > heaviest.mass():
        heaviest = Formula(molecule)
print("heaviest mass\n",heaviest.mass())
print(heaviest)
# find the lightest molecule and print the mass and the formula
lightest = Formula(molecules[0])
for molecule in molecules:
    if Formula(molecule).mass() < lightest.mass():
        lightest = Formula(molecule)
print("\nlightest mass\n", lightest.mass())
#print formula of lightest molecule
print(lightest)

# find the molecule with the highest number of atoms and print the mass and the formula
most_atoms = Formula(molecules[0])
for molecule in molecules:
    if sum(Formula(molecule).get_formula().values()) > sum(most_atoms.get_formula().values()):
        most_atoms = Formula(molecule)
print("\nmost atoms \n", most_atoms.mass())
#print formula of molecule with most atoms
print(most_atoms)


# find the molecule with the lowest number of atoms and print the mass and the formula
least_atoms = Formula(molecules[0])
for molecule in molecules:
    if sum(Formula(molecule).get_formula().values()) < sum(least_atoms.get_formula().values()):
        least_atoms = Formula(molecule)
print("\nleast atoms \n", least_atoms.mass())
#print formula of molecule with least atoms
print(least_atoms)

# average mass of all molecules
average_mass = sum([Formula(molecule).mass() for molecule in molecules]) / len(molecules)
print("\naverage mass \n", average_mass)

# average number of C-Atoms in all molecules
average_C = sum([Formula(molecule).numAtoms('C') for molecule in molecules]) / len(molecules)
print("\naverage number of C-Atoms \n", average_C)
