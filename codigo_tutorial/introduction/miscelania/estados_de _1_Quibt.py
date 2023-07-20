from locale import ABMON_10
import numpy as np
from sympy import *
import pennylane as qml
import sys

# Ajeitar pra pegar a entrada  

#str = sys.argv[1]
#print(str)



brakets = ["|0>","1>","|+>","|->","<0|","<1|","<+|","<-|"]

kets = ["|0>","|1>","|+>","|->"]

bras = ["<0|","<1|","<+|","<-|"]

## Mapeia cada bra com o seu ket correspondente
ketsBrasMap = {
    "<0|": "|0>",
    "<1|": "|1>",
    "<+|": "|+>",
    "<-|": "|->"
}

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
        qml.QubitStateVector(np.array([1/np.sqrt(2), 1/np.sqrt(2)]), wires=range(1))    
    elif ket == "|->" :   
        qml.QubitStateVector(np.array([1/np.sqrt(2), -1/np.sqrt(2)]), wires=range(1))          

    return qml.state()

## Retorna o vetor de estado desejado (um ket ou um bra  )
def preparaEstado(valor) :    
    vetorEstado = None

    if valor in kets :             
        vetorEstado = Matrix(preparaEstado_circuit(valor))                
    
    ## Prepara um bra (transposto conjugado)
    elif valor in bras : # a funcao de conjugado apliacada abaixo nao funciona corretamete em tensores vindos do cirtuico do pennylanne
                         # portanto foi necessario aplica-la ao tipo Matrix e reaplicar o resultato do np.darray 
                         # ao uma nova Matrix
        vetorEstado = Matrix(np.conjugate(Matrix(preparaEstado_circuit(ketsBrasMap[valor])))).T              

    return vetorEstado    

## Calcula produtos exteriores que representam um operador qualquer na base computacional
## Ex.: operador Z = |0><1| + |1><0| 
def calculaMatrizDoOperadorNaBaseComputacional(operador):
    ## Retira espaco em branco 
    operadorSemEspacos = operador.replace(" ","")
    ## continuar aqui e verifica se a string eh maior que 6 
    print(len(operadorSemEspacos))                                                                                                                                                                                                                                                                                                      



#print(preparaEstado("<-|"))
#pprint(preparaEstado("<-|"))
#print(preparaEstado("|+>"))
#pprint(preparaEstado("|+>"))
#pprint(preparaEstado("<-|").dot(preparaEstado("|1>")))

## calcular a matriz do operador Y=−i|0><1|+i|1><0|

## Base Computacional
ket_0 = preparaEstado("|0>")
bra_0 = preparaEstado("<0|")
ket_1 = preparaEstado("|1>")
bra_1 = preparaEstado("<1|")

## Base de Hadamard
ket_mais = preparaEstado("|+>")
bra_mais = preparaEstado("<+|")
ket_menos = preparaEstado("|->")
bra_menos = preparaEstado("<-|")
 
# Multiplica-se e soma-se os prdutos exteriores da expressao  Y=−i|0><1|+i|1><0|

Y = -1j*(ket_0 * bra_1) + 1j*(ket_1 * bra_0)

pprint(Y)

#A00 = bra_mais * Y * ket_mais
#A01 = bra_mais * Y * ket_menos
#A10 = bra_menos * Y * ket_mais
#A11 = bra_menos * Y * ket_menos

## como retorna um matriz 1x1 (um so elemento) pego o valor do mesmo com o indice [0] 
Aij = []
A_mais_mais = (bra_mais * Y * ket_mais)[0]
A_mais_menos = (bra_mais * Y * ket_menos)[0]
A_menos_mais = (bra_menos * Y * ket_mais)[0]
A_menos_menos = (bra_menos * Y * ket_menos)[0]
Aij.append(A_mais_mais)
Aij.append(A_mais_menos)
Aij.append(A_menos_mais)
Aij.append(A_menos_menos)

estadoNaBaseMaisMenoshMap = {
    Aij[0]: "|+><+|",
    Aij[0]: "|+><-|",
    Aij[0]: "|-><+|",
    Aij[0]: "|-><-|"
}
  

pprint(A_mais_mais)
pprint(A_mais_menos)
pprint(A_menos_mais)
pprint(A_menos_menos)
#pprint(bra_mais * Y * ket_mais)
#pprint(bra_mais * Y * ket_menos)
#pprint(bra_menos * Y * ket_mais)
#pprint(bra_menos * Y * ket_menos)