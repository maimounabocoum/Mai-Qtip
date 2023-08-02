import numpy as np
import matplotlib.pyplot as plt
from qutip import *

## Pauli matrices
#print(sigmax())
#print(sigmay())
#print(sigmaz())

PHI = basis(2, 0)
PHI:dnorm()
print(PHI)

