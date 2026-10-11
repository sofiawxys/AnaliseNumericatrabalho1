
#EXERCÍCIO 2

import math

coeficiente = 9/(2*math.sqrt(3))
soma =0

for n in range(0,31):
    termo= math.pow(math.factorial(n),2)/math.factorial(2*n+1)
    soma += termo

    sn = coeficiente * soma
    print('S',n, '= ' , sn)

print('') # linha vazia
print('S= ',sn)
erroabsoluto= abs(math.pi-sn)
print('Erro absoluto= ',erroabsoluto)