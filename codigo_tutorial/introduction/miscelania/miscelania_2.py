import numpy as np
import pennylane as qml

  ## ARQUIVO CRIADO PARA TESTES DIVERSOS

#dev = qml.device("default.qubit", wires=2)


print ("ZI") ## produto tensorial Z @ I
ZI = qml.PauliZ(0) @ qml.Identity(1) 
print(ZI.matrix())
print ()

print ("IZ") ## produto tensorial I @ Z
IZ = qml.Identity(0) @ qml.PauliZ(1)
print (IZ.matrix())
print ()

ZZ = qml.PauliZ(0) @ qml.PauliZ(1) ## produto tensorial Z @ Z
print ("ZZ")
print (ZZ.matrix())
print ()


# Produto escalar/interno (para vetores de uma dimensao). 
# Multipliacao de matrizes
prod1 = np.dot(ZI.matrix(), IZ.matrix()) 
print("PRODUTO")
print(prod1)



#prod1 = qml.math.dot(IZ,ZI)
#print (type(prod1))