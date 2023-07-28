
import numpy as np
import pennylane as qml

from sympy import Matrix, pprint, Number, nsimplify
from sympy.physics.quantum import TensorProduct

#########################################
## Este python é para testtes gerais.
###########################################


## Para deixar um numero em uma formula (expresao) que se aproxime do numero em questao 
## Ex: 0.70710678  corresponde ao racional  √2⋅ⅈ/2 
def formula_expr(expr):    
    return expr.xreplace({n : nsimplify(n) for n in expr.atoms(Number)})


############################################################################################
##  Exemplo de circuito com varias operacoes e a forma de obter a matriz que o representa  ##
############################################################################################
dev = qml.device('default.qubit', wires=1)
@qml.qnode(dev)
def circuit1():
    #qml.BasisState(np.array([1, 1]), wires=range(2)) # prepare |11>
    #return qml.state()    
    qml.PauliX(wires = 0)
    qml.Hadamard(wires = 0)
    return qml.state()
#qml.matrix(circuit1)()
#print()
#pprint(Matrix(circuit1()))
print("######## CIRCUITO 1 ##############")
print()
print(qml.draw(circuit1)())
print()
pprint(qml.matrix(circuit1)())
print()
pprint(formula_expr(Matrix(qml.matrix(circuit1)())))
print()

@qml.qnode(dev)
def circuit2():
    #qml.BasisState(np.array([1, 1]), wires=range(2)) # prepare |11>
    #return qml.state()        
    qml.Hadamard(wires = 0)
    qml.PauliX(wires = 0)
    return qml.state()
#qml.matrix(circuit1)()
#print()
#pprint(Matrix(circuit1()))
print("######## CIRCUITO 2 ##############")
print()
print(qml.draw(circuit2)())
print()
pprint(qml.matrix(circuit2)())
print()
pprint(formula_expr(Matrix(qml.matrix(circuit2)())))
print()

## Somente com as matrizes de cada porta sem executar diretanet um circuito
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



## matriz de porta Hadamard 
H = 1/np.sqrt(2)*Matrix([[1,1],
                        [1,-1]])


X = Matrix([[0,1],[1,0]])

XH = X * H
HX = H * X

pprint(formula_expr(XH))
pprint(formula_expr(HX))
