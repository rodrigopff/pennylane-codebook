import numpy as np
from sympy import *
import pennylane as qml
#from sympy.physics.quantum import TensorProduct
#from sympy import Matrix, pprint

#from sympy.physics.quantum.dagger import Dagger


## Para deixar a precisao dos numero da matriz como se queira
def round_expr(expr, num_digits):
    return expr.xreplace({n : round(n, num_digits) for n in expr.atoms(Number)})
    

## Para deixar um numero em uma formula (expresao) que se aproxime do numero em questao 
## Ex: 0.70710678  corresponde ao racional  √2⋅ⅈ/2 
def formula_expr(expr):    
    return expr.xreplace({n : nsimplify(n) for n in expr.atoms(Number)})

#op = qml.X(wires=0)
print()
opH  = qml.Hadamard(wires=0)
print(qml.matrix(opH))
print()
pprint(Matrix(qml.matrix(opH)))
print()
pprint(formula_expr(Matrix(qml.matrix(opH))))
print()
opX  = qml.PauliX(wires=0)
print(qml.matrix(opX))
print()
pprint(Matrix(qml.matrix(opX)))
print()

############################################################################################
##  Exemplo de circuito com varias operacoes e a forma de obter a matriz que o representa  ##
############################################################################################
dev = qml.device('default.qubit', wires=1)
@qml.qnode(dev)
def circuit1():
    #qml.BasisState(np.array([1, 1]), wires=range(2)) # prepare |11>
    #return qml.state()
    #qml.PauliX(wires=0)
    #qml.PauliZ(wires=0)
    qml.PauliZ(wires=0)
    qml.PauliX(wires=0)

    return qml.state()
#qml.matrix(circuit1)()
print()
print(qml.draw(circuit1)())
print()
pprint(qml.matrix(circuit1)())
print()
pprint(Matrix(qml.matrix(circuit1)()))
print()


###################################################
##  Exemplo de circuito para preparar um estado  ##
###################################################
dev2 = qml.device('default.qubit', wires=2)
@qml.qnode(dev2)
def preparaEstado_circuit():
    qml.QubitStateVector(np.array([0, -1j/np.sqrt(2), 0, 1j/np.sqrt(2)]), wires=range(2))    
    return qml.state()

print(preparaEstado_circuit())

# Vetor coluna que representa o estado retornado pelo circuito
matrizColuna = Matrix(preparaEstado_circuit())

## Imprime a representacao matricial do estado 
# Na forma racional se for necessario 
print()
pprint(formula_expr(matrizColuna)) # |ket>
print()
pprint(formula_expr(Matrix(np.conjugate(matrizColuna)).T)) # <bra|

# Na forma numericao com o arrendondamento adequado
#pprint(round_expr(matrizColuna,2)) # |ket>
#pprint(round_expr(Matrix(np.conjugate(matrizColuna)).T,2)) # <bra|


## Vetor coluna
print()
teste1 = Matrix([1, 0])
pprint(teste1)                 

## Vetor linha
print()
teste2 = Matrix([[1, 0]])
pprint(teste2)                 

# Multiplica as matrizes retorna matrizes  (msemo que seja de um so elemento)
print()
pprint(teste1*teste2)
print()
pprint(teste2*teste1)

# Faz um produto interno (inner product) utilizando a funcao ".dot()" entre os dois vetores (por ex. um produto <bra|ket>)
# Retorna um escalar
print()
pprint(teste2.dot(teste1))
print()
#print()
#n = nsimplify(-0.8660254037844386j)
#pprint(n)
#print(np.sqrt(3)/2)


ter = Matrix([
[0, 1],
[2, 3]])

pprint(ter*ter)

