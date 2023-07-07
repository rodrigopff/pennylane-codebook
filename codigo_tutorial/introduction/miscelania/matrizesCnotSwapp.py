from sympy import Matrix, pprint
from sympy.physics.quantum import TensorProduct
import numpy as np

#m1 = Matrix([[1,2],[3,4]])
#m2 = Matrix([[1,0],[0,1]])

#pprint(m1*m2)
#pprint(m1)
#pprint(m2)

#t = TensorProduct(m1, m2)
#pprint(t)


## A matriz da porta CNOT
CNOTMatriz = Matrix([[1.0, 0, 0, 0],
			        [0, 1.0, 0, 0],
                    [0, 0, 0, 1.0],
                    [0, 0, 1.0, 0]])
print()
print("##################")
print("##  PORTA CNOT  ##")
print("##################")
print()
pprint(CNOTMatriz)                            
print()

## Gera um tensorial de duas portas Hadamard HxH
H = 1/np.sqrt(2)*Matrix([[1,1],
                        [1,-1]])

print()
print("####################")
print("## PORTA HADAMARD ##")
print("####################")
print()
pprint(H)
print()


print()
print("##########################################################")
print("## PORTA H ⊗ H (PRODUTO TENSORIAL ENTRE DUAS PORTAS H) ##")
print("##########################################################")
HXH = TensorProduct(H,H)
print()
pprint(HXH)
print()
 

## Gera o circuito que troca a ordem dos bits alvo (target) e de conrole (control)
## Bit alvo agora é o primeiro qbit e o bit de controle é o segundo qbit
## Vide o livro do COMBARRO E CASTILLO pag. 29 e 30.
## Lá existe a descricao da porta  CNOT invertida e de como usá-la com mais duas pras CNOT usuais 
# para gerar uma porta de SWAPP 
CNOTMatrizComInversaoDeQbits = HXH*CNOTMatriz*HXH 
print()
print("###########################################################")
print("## PORTA CNOT COM OS QBITS ALTO E DE CONTROLE INVERTIDOS ##")
print("###########################################################")
print()
pprint(CNOTMatrizComInversaoDeQbits)
print()


## Gera a matriz da porta de swap (vide livro do COMBARRO E CASTILLO inicio da pag.30)
swapMatriz = CNOTMatriz*CNOTMatrizComInversaoDeQbits*CNOTMatriz
print()
print("###################")
print("## PORTA DE SWAP ##")
print("###################")
print()
pprint(swapMatriz)
print()