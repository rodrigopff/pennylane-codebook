import numpy as np
import pennylane as qml

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
    ## A operacao que leva os tensorais IZ e ZI combinados para  o tensorial ZZ
    ## é uma multiplicacao de matrizes (produto interno np.dot(ZI.matrix(), IZ.matrix()))
    ## No nosso caso como os vetores de valores esperados sao unidimensionais 
    ## temos que efetuar a multiplicacao de cada elemento do vetor termo a termo 
    ## (somando os valores é claro) e armazenando no vetor de resultados na mesmas posicoes
    ## Nao se trata de um produto escalar comum como o np.dot()
    for i in range(len(ZI_results)):
        res = ZI_results[i] * IZ_results[i]
        combined_results[i] = res
    return combined_results

 
theta = np.linspace(0, 2 * np.pi, 100)

# Run circuit 1, and process the results
circuit_1_results = np.array([circuit_1(t) for t in theta])

ZI_results = circuit_1_results[:, 0]
IZ_results = circuit_1_results[:, 1]
combined_results = zi_iz_combination(ZI_results, IZ_results)

# Run circuit 2
ZZ_results = np.array([circuit_2(t) for t in theta])

# Plot your results
## A funcao plotter esta definida apenas no Pennylane
plot = plotter(theta, ZI_results, IZ_results, ZZ_results, combined_results)
