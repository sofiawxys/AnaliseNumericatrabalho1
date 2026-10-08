
#Exercício 3

import math

tolerancia= math.pow(10,-5)
termo =4 #Primeiro termo
n=0
soma=0

while abs(termo) >= tolerancia:
    soma += termo
    n += 1
    termo = 4 * (math.pow(-1, n) / (2 * n + 1))

print("Número de termos somados= ",n ," Soma= ",soma)
erroabsoluto= abs(math.pi-soma)
print("Erro Absoluto= ",erroabsoluto)