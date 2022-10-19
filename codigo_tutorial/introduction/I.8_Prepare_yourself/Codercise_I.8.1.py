dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY OPERATIONS TO PREPARE THE TARGET STATE
    # O estado em questao tem u fae global que pdoe ser desprezada.
    # Quando se aplica a Porta RZ termina-se com 
    # um numero complexo na frente  de cada ket (5.pi/8) , porem com mostado na
    # secao I.5 pode-se fatorar o fase e colocal-a de fora o que torna 
    # o estado tendo uma só fase no  ket |1>
    qml.Hadamard(wires=0)
    qml.RZ(5*(np.pi/4),wires=0)
    
    # Pode-se aplicar 5 vzs tb a porta T que da o mesmo resultado
    #qml.T(wires=0)
    #qml.T(wires=0)
    #qml.T(wires=0)
    #qml.T(wires=0)
    #qml.T(wires=0)
    
    return qml.state()