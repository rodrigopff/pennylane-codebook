from sympy import *

## Exemplo de como imprimir expressao matematicas  bonitinhas com o pprint
x, y, z = symbols('x y z')

## Se o terminal suportar unicode ##
pprint(Integral(sqrt(1/x), x), use_unicode=True)


## Se o terminal nao suportar unicode ##
pprint(Integral(sqrt(1/x), x), use_unicode=False)