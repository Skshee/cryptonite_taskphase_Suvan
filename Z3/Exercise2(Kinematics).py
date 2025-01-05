#Ima Hurryin is approaching a stoplight moving with a velocity of 30.0 m/s. The light turns yellow, and Ima applies the brakes and skids to a stop. If Ima's acceleration is -8.00 m/s2, then determine the displacement of the car during the skidding process.

from z3 import *

d, a, v_i, v_f, t = Reals('d a v_i v_f t')

equations = [
    d == v_i * t + (1/2)*(a*t**2),
    v_f == v_i + a*t,
]

problems = [
    v_i == 30,
    v_f == 0,
    a == -8,
]

s = Solver()
s.add(equations + problems)
print(s.check())
print(s.model())

# Mistake I made : Used Real instead of Reals









