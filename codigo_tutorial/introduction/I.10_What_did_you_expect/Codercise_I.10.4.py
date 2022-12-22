import numpy as np
import pennylane as qml

## Este exercicio deve ser visto com muito cuidado no que diz respeito a implementacao da segunda funcao
## variance_scaling(n_shots).
## esta funcao na realidade deve ser baseada no grafico plotado pelo resutado da funcao variance_experiment(n_shots) 
## Com base nos resultados do grafico verificamos que os pontos pltados aproximam-se por uma funcao que é inversamente proporcional a numero de 
## disparos (n_shots). Portanto a funcao deve retoanr algum valor do tipo 1/n_shots

def variance_experiment(n_shots):
    """Run an experiment to determine the variance in an expectation
    value computed with a given number of shots.
    
    Args:
        n_shots (int): The number of shots
        
    Returns:
        float: The variance in expectation value we obtain running the 
        circuit 100 times with n_shots shots each.
    """

    # To obtain a variance, we run the circuit multiple times at each shot value.
    n_trials = 100

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE A DEVICE WITH GIVEN NUMBER OF SHOTS
    dev = qml.device("default.qubit", wires=1, shots=n_shots)

    # DECORATE THE CIRCUIT BELOW TO CREATE A QNODE
    @qml.qnode(dev)
    def circuit():
        qml.Hadamard(wires=0)
        return qml.expval(qml.PauliZ(wires=0))

    # RUN THE QNODE N_TRIALS TIMES AND RETURN THE VARIANCE OF THE RESULTS
    resultado = 0
    resultadoSomaSimples = 0
    resultadoSomaQuadrado = 0
    for i in range(n_trials):        
        # calculando o valor esperado diretamente da definicao de variancia:
        # valor_esperado = medias_dos_quadrados - quadrado_da_media 
        # Em simbolos : sigma² = <X²> - <X>²         
        resultado = circuit()
        resultadoSomaSimples = resultadoSomaSimples + resultado    
        resultadoSomaQuadrado = resultadoSomaQuadrado + resultado**2    
    return resultadoSomaQuadrado/n_trials - (resultadoSomaSimples/n_trials)**2

    

def variance_scaling(n_shots):
    """Once you have determined how the variance in expectation value scales
    with the number of shots, complete this function to programmatically
    represent the relationship.
    
    Args:
        n_shots (int): The number of shots
        
    Returns:
        float: The variance in expectation value we expect to see when we run
        an experiment with n_shots shots.
    """

    estimated_variance = 0

    ##################
    # YOUR CODE HERE #
    ##################

    # ESTIMATE THE VARIANCE BASED ON SHOT NUMBER
    # Os pontoa plotados indicam que podemos estimar o valor por um funcao que é inversamente proporcional ao numero de disparos (n_shots)
    estimated_variance = 1/n_shots
    return estimated_variance

# Various numbers of shots; you can change this
shot_vals = [10, 20, 40, 100, 200, 400, 1000, 2000, 4000]

# Used to plot your results
results_experiment = [variance_experiment(shots) for shots in shot_vals]
results_scaling = [variance_scaling(shots) for shots in shot_vals]
plot = plotter(shot_vals, results_experiment, results_scaling)