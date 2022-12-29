import numpy as np
import pennylane as qml

dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.
    
    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    # Converte decimal para um binario e completa o tamanho dos quibits caso o numero basis_id
    # convertido para binario seja menor que o numero de qbits bo circuito.
    numero = np.binary_repr(basis_id,3) 
    
    # Salva numa lista (vetor) 
    numeroListaStrings = list(numero)
    
    # Converte a lista gerada como uma lista de strings (chars) para uma lista de inteiros
    numeroListaInteiro = list(map(int, numeroListaStrings))
    basis_state = numeroListaInteiro
    
    # CREATE THE BASIS STATE
    qml.BasisStatePreparation(basis_state, wires=range(3))
    return qml.state()


basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")