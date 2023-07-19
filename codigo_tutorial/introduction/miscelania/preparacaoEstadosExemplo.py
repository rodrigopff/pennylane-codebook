import numpy as np
import pennylane as qml

dev = qml.device('default.qubit', wires=2)
@qml.qnode(dev)
def example_circuit():
    qml.BasisState(np.array([1, 1]), wires=range(2)) # prepare |11>
    return qml.state()
print(example_circuit())