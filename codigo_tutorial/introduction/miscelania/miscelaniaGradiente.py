import numpy as np
import pennylane as qml

dev1 = qml.device("default.qubit", wires=1)

@qml.qnode(dev1)
def circuit2(phi1, phi2):
    qml.RX(phi1, wires=0)
    qml.RY(phi2, wires=0)
    return qml.expval(qml.PauliZ(0))

## as duas linhas abaixo funfam tb
#draw = qml.draw(circuit2)
#print(draw(0.54, 0.12))
print()
print(qml.draw(circuit2)(0.54, 0.12))
# print(qml.draw(circuit2)(0, 0))
#print(type(circuit2(0,0)))


print()
dcircuit = qml.grad(circuit2, argnum=[0, 1])
print(dcircuit(0.54, 0.12))
#print(circuit2(0.54, 0.12))