dev = qml.device("default.qubit", wires=1)

##################
# YOUR CODE HERE #
##################

# ADJUST THE VALUES OF PHI, THETA, AND OMEGA
#phi, theta, omega = 0.0, 0.0, 0.0


theta = (np.pi)/2
phi = (np.pi)/2
omega = (np.pi)/2


@qml.qnode(dev)
def hadamard_with_rz_rx():
    qml.RZ(phi, wires=0)
    qml.RX(theta, wires=0)
    qml.RZ(omega, wires=0)
    return qml.state()
    
#print(hadamard_with_rz_rx())