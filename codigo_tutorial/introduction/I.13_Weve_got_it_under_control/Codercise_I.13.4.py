import numpy as np
import pennylane as qml


dev = qml.device('default.qubit', wires=4)

@qml.qnode(dev)
def four_qubit_mcx():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT ABOVE USING A 4-QUBIT MULTI-CONTROLLED X
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    
    # O parametro  control_wires=[0, 1, 2, 3] conforme é indicado no tutorial está depreciado
    # Basta usar o parametro wires = [0, 1, 2, 3] onde o ultomo bit é o bit alvo
    # Ex.: no lugar de 
    # qml.MultiControlledX(control_wires=[0, 1, 2, 3], wires=4, control_values="1011")
    # podemos ter 
    # qml.MultiControlledX(wires=[0, 1, 2, 3], control_values="1011")    

    qml.MultiControlledX(wires=[0, 1, 2, 3], control_values="001")
    return qml.state()
    
print(four_qubit_mcx())   