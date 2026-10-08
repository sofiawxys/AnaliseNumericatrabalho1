
#Exercício 2

import math

#Definição da constante
k = 9/(2*math.sqrt(3))
soma =0


for n in range(0,31):
    termo= math.pow(math.factorial(n)**2)/math.factorial(2*n+1)
    soma += termo

    sn = k * soma
    print("S",n, ": ", sn)

print('')
print("S= ",sn)
erroabsoluto= abs(math.pi-soma)
print("Erro absoluto= ",erroabsoluto)