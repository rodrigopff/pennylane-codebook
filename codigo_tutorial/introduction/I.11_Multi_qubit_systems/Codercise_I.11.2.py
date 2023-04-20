import numpy as np
import pennylane as qml

# Importando para desenhar os circuitos bonitinhos 
import matplotlib.pyplot as plt

# Creates a device with *two* qubits
dev = qml.device('default.qubit', wires=2)
#dev = qml.device("qiskit.aer", wires=2)

@qml.qnode(dev)
def two_qubit_circuit():
#def circuit():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE |+>|1>
    qml.Hadamard(wires=0)
    qml.PauliX(wires=1)

    # RETURN TWO EXPECTATION VALUES, Y ON FIRST QUBIT, Z ON SECOND QUBIT
    res1 = qml.expval(qml.PauliX(0))
    res2 = qml.expval(qml.PauliZ(1))
    return [res1,res2]

#print(two_qubit_circuit())

print(two_qubit_circuit())

#print(qml.draw(circuit2)(0.54, 0.12))

## PARA DESENHAR O CICUITO COM MATPLOT O NOME DA CIRCUITO NAO PODE TER UNDESCORE "_"
## DEVE-SE TROCAR O NOME ACIMA PRA FUNFAR 
# Desenha o circuito
#draw = dev._two_qubit_circuit.draw(output="mpl")

#draw = dev._circuit.draw(output="mpl")
# draw("mlp")
#plt.show()

print(qml.draw(two_qubit_circuit)())