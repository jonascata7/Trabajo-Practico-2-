
numeros = []

for i in range(10):
    num = int(input(f"Ingrese el número para la posición {i + 1}: "))
    numeros.append(num)

print("\n---------------------------------------------")
print("Los números en orden inverso son:")

# 3. Bucle para mostrar los números al revés
for i in range(9, -1, -1):
    print(f"Posición {i + 1}: {numeros[i]}")