import numpy as np
from sympy import *
import pennylane as qml


############################################################
##  Exemplo de circuito para preparar um estado de 1 qbit ##
############################################################
dev = qml.device('default.qubit', wires=1)
@qml.qnode(dev)
def preparaEstado_circuit(ket):
    if ket == "|0>" :   
        qml.QubitStateVector(np.array([1, 0]), wires=range(1))
    elif ket == "|1>" :   
        qml.QubitStateVector(np.array([0, 1]), wires=range(1))    
    elif ket == "|+>" :
        qml.QubitStateVector(np.array([1j/np.sqrt(2), 1j/np.sqrt(2)]), wires=range(1))    
    elif ket == "|->" :   
        qml.QubitStateVector(np.array([1j/np.sqrt(2), -1j/np.sqrt(2)]), wires=range(1))    
    return qml.state()

## Retorna o vetor de estado desejado (um ket ou um bra  )
def preparaEstado(valor, tipoVetor):

    if tipoVetor =="ket":
       vetorEstado = Matrix(preparaEstado_circuit(valor))       
    elif tipoVetor =="bra":
       vetorEstado = Matrix(preparaEstado_circuit(valor)).T
    return vetorEstado   

## Calcula produtos exteriores que representam um operador qualquer na base computacional
## Ex.: operador Z = |0><1| + |1><0| 

def calculaMatrizDoOperadorNaBaseComputacional(operador):
    ## Retira espaco em branco 
    operadorSemEspacos = operador.replace(" ","")
    ## continuar aqui e verifica se a string eh maior que 6 
    print(len(operadorSemEspacos))

calculaMatrizDoOperadorNaBaseComputacional("|0><1| + |1><0|")

#matrizColuna = preparaEstado("|->","ket")
#pprint(matrizColuna)

