numeros = [45, 12, 89, 23, 67, 4, 55, 90, 31, 78]

numero_buscado = int(input("Ingrese el número que desea buscar: "))

i = 0
encontrado = False

while i < 10 and not encontrado:
    if numeros[i] == numero_buscado:
        encontrado = True
    else:
        i += 1

print("---------------------------------------------")
if encontrado:
    print(f"¡Encontrado! El número {numero_buscado} está en la posición: {i + 1}")
else:
    print(f"El número {numero_buscado} no se encuentra en el arreglo.")