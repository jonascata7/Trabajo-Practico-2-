import random

numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

print("Lista de números aleatorios:")
print(numeros)

mayor = numeros[0]
menor = numeros[0]

for i in range(1, 15):
    if numeros[i] > mayor:
        mayor = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]

print("---------------------------------------------")
print(f"El número más GRANDE es: {mayor}")
print(f"El número más PEQUEÑO es: {menor}")