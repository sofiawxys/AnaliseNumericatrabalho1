
#EXERCÍCIO 2

import math

coeficiente = 9/(2*math.sqrt(3))
soma =0

for n in range(1,31):
    k=n-1# índice k varia de 0 a n-1 para garantir a soma de n termos
    termo= math.pow(math.factorial(k),2)/math.factorial(2*k+1)
    soma += termo

    sn = coeficiente * soma
    print('S',n, '= ' , sn)

print('') # linha vazia
print('S= ',sn)
erroabsoluto= abs(math.pi-sn)
print('Erro absoluto= ',erroabsoluto)