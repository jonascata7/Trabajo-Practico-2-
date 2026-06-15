opcion = 0

while opcion != 5:
    print("\n--- MENÚ CALCULADORA ---")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    opcion = int(input("Elija una opción: "))
    
    if 1 <= opcion <= 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == 1:
            print(f"Resultado: {num1 + num2}")
        elif opcion == 2:
            print(f"Resultado: {num1 - num2}")
        elif opcion == 3:
            print(f"Resultado: {num1 * num2}")
        elif opcion == 4:
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: No se puede dividir por cero.")
    elif opcion == 5:
        print("Saliendo de la calculadora... ¡Chau!")
    else:
        print("Opción inválida. Intente de nuevo.")