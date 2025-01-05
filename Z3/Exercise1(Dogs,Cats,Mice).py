#Consider the following puzzle. Spend exactly 100 dollars and buy exactly 100 animals. Dogs cost 15 dollars, cats cost 1 dollar, and mice cost 25 cents each. You have to buy at least one of each. How many of each should you buy?

from z3 import *

Dogs = Int('Dog')
Cats = Int('Cat')
Mice = Int('Mice')

solver = Solver()
solver.add(Dogs>=1)
solver.add(Cats>=1)
solver.add(Mice>=1)
solver.add(Dogs*15+Cats*1+Mice*0.25<=100)
solver.add(Dogs+Cats+Mice==100)

print(solver.check())
print(solver.model())

# Mistake 1 : Converted all animals to Real type but they cannot be real as we can't have decimal animals
# Mistake 2 : Assigned values to animals directly using the wrong logic



