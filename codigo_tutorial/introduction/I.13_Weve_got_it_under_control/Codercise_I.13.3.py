import numpy as np
import pennylane as qml


dev = qml.device("default.qubit", wires=3)

# Prepare first qubit in |1>, and arbitrary states on the second two qubits
#phi, theta, omega = 1.2, 2.3, 3.4
phi, theta, omega = 0.5, 0.1, 1.03


## Criei esta funcao porque o tutorial tem a funcao mas não é exibida na corpo do texto
@qml.qnode(dev)
def prepare_states(phi, theta, omega):
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY OPERATIONS TO PREPARE THE STATE
    qml.RX(phi,wires=0)
    qml.RY(theta,wires=1)
    qml.RZ(omega,wires=1)

    return qml.state()


# A helper function just so you can visualize the initial state
# before the controlled SWAP occurs.
@qml.qnode(dev)
def no_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)
    return qml.state()


@qml.qnode(dev)
def controlled_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)
    
    ##################
    # YOUR CODE HERE #
    ##################

    # PERFORM A CONTROLLED SWAP USING A SEQUENCE OF TOFFOLIS
    qml.Toffoli(wires=[0, 1, 2])
    qml.Toffoli(wires=[0, 2, 1])
    qml.Toffoli(wires=[0, 1, 2])

    return qml.state()


print(no_swap(phi, theta, omega))
print(controlled_swap(phi, theta, omega))
