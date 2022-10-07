dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def my_circuit(theta, phi, omega):
    qml.RX(theta, wires=0)
    qml.RY(phi, wires=1)
    qml.RZ(omega, wires=2)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 0])
    return qml.probs(wires=[0, 1, 2])


##################
# YOUR CODE HERE #
##################
resource_calculator = qml.specs(my_circuit)
theta, phi, omega = 0.1, 0.2, 0.3
depth  = resource_calculator(theta, phi, omega)

resources  = resource_calculator(theta, phi, omega)
# FILL IN THE CORRECT CIRCUIT DEPTH
print (type(resources))
print (resources)
print (resources['depth'])
depth = resources['depth']