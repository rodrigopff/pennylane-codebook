import numpy as np
import pennylane as qml

  ## ARQUIVO CRIADO PARA TESTES DIVERSOS


def variance_experiment(n_shots):

 
    dev = qml.device('default.qubit', wires=1, shots=n_shots)
    n_trials = 100
    @qml.qnode(dev)
    def circuit():
        ##################
        # YOUR CODE HERE #
        ##################         
        qml.Hadamard(wires=0)    
        return qml.expval(qml.PauliZ(wires=0))           
        #return qml.sample(qml.PauliZ(wires=0))       
    #circuit = circuit()     
    resultado = 0
    resultadoSomaSimples = 0
    resultadoSomaQuadrado = 0
    for i in range(n_trials):
       resultado = circuit()
       resultadoSomaSimples = resultadoSomaSimples + resultado
       resultadoSomaQuadrado = resultadoSomaQuadrado + resultado**2
    return resultadoSomaQuadrado/n_trials - (resultadoSomaSimples/n_trials)**2
estimated_expval = 0
shot_vals = [10, 20, 40, 100, 200, 400, 1000, 2000, 4000]

    #for sample in circuit:
    #    estimated_expval = estimated_expval + sample        

results_experiment = [variance_experiment(shots) for shots in shot_vals]
print(results_experiment)
#print(variance_experiment())
#print()
