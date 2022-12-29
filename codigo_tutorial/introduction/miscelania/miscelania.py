import numpy as np
import pennylane as qml

  ## ARQUIVO CRIADO PARA TESTES DIVERSOS

dev = qml.device('default.qubit', wires=2)

@qml.qnode(dev)
def circuit_1(theta):
    """Implement the circuit and measure Z I and I Z.
    
    Args:
        theta (float): a rotation angle.
        
    Returns:
        float, float: The expectation values of the observables Z I, and I Z
    """
    ##################
    # YOUR CODE HERE #
    ##################  
    qml.RX(theta,wires=0)
    qml.RY(2*theta,wires=1)
    res1 = qml.expval(qml.PauliZ(0))
    res2 = qml.expval(qml.PauliZ(1))

    return res1, res2

theta = np.linspace(0, 2 * np.pi, 100)

# Run circuit 1, and process the results
circuit_1_results = np.array([circuit_1(t) for t in theta])

#print(circuit_1_results.shape)
#print(circuit_1_results)


@qml.qnode(dev)
def circuit_2(theta):
    """Implement the circuit and measure Z Z.
    
    Args:
        theta (float): a rotation angle.
        
    Returns:
        float: The expectation value of the observable Z Z
    """ 

    ##################
    # YOUR CODE HERE #
    ################## 
    qml.RX(theta,wires=0)
    qml.RY(2*theta,wires=1)    
    
    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1))

# Run circuit 2
ZZ_results = np.array([circuit_2(t) for t in theta])
print(ZZ_results)
#print(ZZ_results.shape)


ZI_results = circuit_1_results[:, 0]
IZ_results = circuit_1_results[:, 1]

#print(ZI_results)
#print(IZ_results)

#combined_results = np.zeros(len(ZI_results))
#print(combined_results)
def zi_iz_combination(ZI_results, IZ_results):
    """Implement a function that acts on the ZI and IZ results to
    produce the ZZ results. How do you think they should combine?

    Args:
        ZI_results (array[float]): Results from the expectation value of 
            ZI in circuit_1.
        IZ_results (array[float]): Results from the expectation value of 
            IZ in circuit_1.

    Returns:
        array[float]: A combination of ZI_results and IZ_results that 
        produces results equivalent to measuring ZZ.
    """

    combined_results = np.zeros(len(ZI_results))

    ##################
    # YOUR CODE HERE #
    ################## 
    for i in range(len(ZI_results)):
        #(ZI_results[i] + IZ_results[i])/2
        combined_results[i] = (ZI_results[i] + IZ_results[i])/2
    return combined_results

combined_results = zi_iz_combination(ZI_results, IZ_results)
print(combined_results)   