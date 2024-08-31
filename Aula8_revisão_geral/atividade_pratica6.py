lista_numeros = [5, 12, 23, 45, 67, 89, 34.5, 78.9, 0, -12]
pares = []
impares = []

for num in lista_numeros:
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)

print('Par: ', len(pares))
print