
#EXERCÍCIO 1

v=1
i=0 # número de iterações

while 1+v > 1:
    v=v/2
    i=i+1

eps = v*2 # o epsilon máquina é o último valor que alterou a soma

print ('Epsilon máquina=', eps)
print ('Número de iterações=', i-1)

