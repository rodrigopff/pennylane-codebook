dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def too_many_ts():
    """You can implement the original circuit here as well, it may help you with
    testing to ensure that the circuits have the same effect.

    Returns:
        array[float]: The measurement outcome probabilities.
    """
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    
    qml.T(wires=0)
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=2)
    
    qml.T(wires=0)
    
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    
    qml.adjoint(qml.T)(wires=0)
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=2)
    
    qml.adjoint(qml.T)(wires=0)
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=2)
    
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=2)
    
    qml.T(wires=1)
    
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    
    return qml.probs(wires=[0, 1, 2])

@qml.qnode(dev)
def just_enough_ts():
    """Implement an equivalent circuit as the above with the minimum number of 
    T and T^\dagger gates required.

    Returns:
        array[float]: The measurement outcome probabilities.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT, BUT COMBINE AND OPTIMIZE THE GATES
    # TO MINIMIZE THE NUMBER OF TS
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    
    qml.S(wires=0)
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=2)
    
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    
    qml.adjoint(qml.S)(wires=0)
    qml.PauliZ(wires=1)
    qml.adjoint(qml.S)(wires=2)
    
    qml.adjoint(qml.T)(wires=2)
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    
    qml.Hadamard(wires=2)
    return qml.probs(wires=[0, 1, 2])
##################
# YOUR CODE HERE #
##################

# FILL IN THE CORRECT VALUES FOR THE ORIGINAL CIRCUIT
## A profundidade do circuito parece ser 9 mas na realidade é 8. Lembre-se
## que quando possivelm operacoes sao efetuadas em qubits diferentes 
## deve-se deslocar as operacoes (portas etc..) para a esquerda 
## pois operacoes em qubits diferentes podem ser realizadas em paralelo. 
## Vide a licao I.2 deste tutorial.
original_depth = 8

original_t_count = 13
original_t_depth = 6

# FILL IN THE CORRECT VALUES FOR THE NEW, OPTIMIZED CIRCUIT
optimal_depth = 6
optimal_t_count = 3
optimal_t_depth = 2

## retorna as informacoes sobre o circuito
resource_calculator = qml.specs(too_many_ts)
print(resource_calculator())

print("")
print("")


## Compara as medidas dos circuitos. Existem difencas  muito pequenas de precisao
print("******************************* Circuito original *************************************")
print(too_many_ts())
print("***************************************************************************************")

print("***********************Circuito otimizado com menos portas T e T* *********************")
print(just_enough_ts())
print("***************************************************************************************")