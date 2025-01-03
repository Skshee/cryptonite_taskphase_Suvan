from z3 import *

p = Bool('p')
q = Bool('q')
r = Bool('r')

solve(Implies(p, q), r == Not(q), Or(Not(p), r))

# Implies(p, q) is a constraint that means that if p is True, q is True, but if p is False, q can be True or False. It is the logical implication.

#The r == Not(q) is pretty straightforward. The Or(Not(p), r) is a constraint that establishes that p must be False OR r must be True, or both.