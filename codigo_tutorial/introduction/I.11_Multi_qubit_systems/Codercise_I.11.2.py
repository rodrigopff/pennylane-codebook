import numpy as np
import pennylane as qml

# Creates a device with *two* qubits
dev = qml.device('default.qubit', wires=2)

@qml.qnode(dev)
def two_qubit_circuit():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE |+>|1>
    qml.Hadamard(wires=0)
    qml.PauliX(wires=1)

    # RETURN TWO EXPECTATION VALUES, Y ON FIRST QUBIT, Z ON SECOND QUBIT
    res1 = qml.expval(qml.PauliY(0))
    res2 = qml.expval(qml.PauliZ(1))
    return [res1,res2]

print(two_qubit_circuit())