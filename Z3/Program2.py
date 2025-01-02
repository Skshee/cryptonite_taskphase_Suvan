'''
Question
square * square + circle = 16
triangle * triangle * triangle = 27
triangle * square = 6

Find : square * triangle * circle
'''


from z3 import *

square = Int('square')
circle = Int('circle')
triangle = Int('triangle')

solver = Solver()

solver.add(square * square + circle == 16)
solver.add(triangle * triangle * triangle == 27)
solver.add(triangle * square == 6)

solver.check()
print(solver.model())

if solver.check() == sat:
    model = solver.model()

circle_val = model.eval(circle).as_long()
triangle_val = model.eval(triangle).as_long()
square_val = model.eval(square).as_long()

result = square_val * circle_val * triangle_val

print(result)