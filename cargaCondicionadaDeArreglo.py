numeros = []
cantidad = 0

while cantidad < 20:
    num = int(input("Ingrese un número positivo (o negativo para terminar): "))
    if num < 0:
        break  
    numeros.append(num)
    cantidad += 1

if cantidad > 0:
    suma = 0
    for n in numeros:
        suma += n
    promedio = suma / cantidad
    print(f"\nSe ingresaron {cantidad} números.")
    print(f"El promedio es: {promedio}")
else:
    print("\nNo se ingresaron números positivos.")