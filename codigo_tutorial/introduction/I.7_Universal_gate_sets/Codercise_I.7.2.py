dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def convert_to_rz_rx():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT IN THE PICTURE USING ONLY RZ AND RX
    # Hadamard - |H|
    qml.RZ(np.pi/2, wires=0)
    qml.RX(np.pi/2, wires=0)
    qml.RZ(np.pi/2, wires=0)
    
    # |S|---> |T|(dagger)
    # é o mesmo que RZ(pi/2) --> RZ(-pi/4) que é igual a RZ(pi/4)
    qml.RZ(np.pi/4, wires=0)
    
    # |Y| -- Lembre-se Y pode ser escrito como:
    #     Y = iXZ = i.RX(pi)RZ(pi)
    qml.RX(np.pi, wires=0)
    qml.RZ(np.pi, wires=0)
    


    return qml.state()