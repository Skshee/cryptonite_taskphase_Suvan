from z3 import *

x = Int('x')
y = Int('y')

constraints = [
    x + y > 10,
    x - y < 5
]

s = Solver()
s.add(constraints)

if s.check() == sat:
    print("Solution:", s.model())
else:
    print("No solution")

