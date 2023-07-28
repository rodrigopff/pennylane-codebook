import numpy as np
import pennylane as qml

#0.54, 0.12
resultado1 = -np.sin(0.54) * np.cos(0.12)
resultado2 = -np.sin(0.12) * np.cos(0.54)
print(resultado1)
print(resultado2)


print(np.cos(0.54) * np.cos(0.12))


#print(np.cos(3.15826563) * np.cos(-0.01026563))

print("ROTACAO  EM Y")
print(np.cos(7.15266381e-18) * np.cos(3.14159265e+00))
print()
print("ROTACAO  EM X")
print(np.cos(3.14159265e+00) * np.cos(7.15266381e-18))
#7.15266381e-18 3.14159265e+00