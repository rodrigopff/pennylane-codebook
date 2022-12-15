#################### PARTE a) do exercicio

#################
# YOUR CODE HERE #
##################

# WRITE A QUANTUM FUNCTION THAT PREPARES (1/2)|0> + i(sqrt(3)/2)|1>

def prepare_psi():
    
    qml.RX((2*np.pi)/3,wires=0)
    qml.PauliZ(wires=0)


# WRITE A QUANTUM FUNCTION THAT SENDS BOTH |0> TO |y_+> and |1> TO |y_->
def y_basis_rotation():
    
    qml.Hadamard(wires=0)
    qml.S(wires=0)




#################### PARTE b) do exercicio

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def measure_in_y_basis():
    ##################
    # YOUR CODE HERE #
    ##################
    
    # PREPARE THE STATE
    prepare_psi()

    # PERFORM THE ROTATION BACK TO COMPUTATIONAL BASIS
     # o adjunto é o transposto conjugado. É aplicado o adjunto na funcao que esta entre parenteses. 
    # O Adjunto de uma funcao é aplicado na ordem inversa das portas que sao apliacadas na funcao. No nosso ex. a funcao
    # aplica uma porta Hadamard e depois uma porta S ao estado. O adjunto será feito na ordem inversa : adjunto de S ao estado e depois adjunto de H ao estado.
    qml.adjoint(y_basis_rotation)()

    # RETURN THE MEASUREMENT OUTCOME PROBABILITIES

    return qml.probs(wires=0)

print(measure_in_y_basis())