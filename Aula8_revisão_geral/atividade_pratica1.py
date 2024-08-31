lista_numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = []
for par in lista_numeros:
    if par % 2 == 0:
        numeros_pares.append(par)

print(numeros_pares)