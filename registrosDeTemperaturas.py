temps = []

print("--- Registro de Temperaturas ---")
for i in range(7):
    t = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    temps.append(t)

opcion = ""
while opcion.upper() != "D":
    print("\n--- MENÚ CONSULTAS ---")
    print("A) Ver todas las temperaturas\nB) Ver el promedio\nC) Ver el día más caluroso\nD) Salir")
    opcion = input("Elija una opción: ").upper()
    
    if opcion == "A":
        for i in range(7):
            print(f"Día {i + 1}: {temps[i]}°C")
    elif opcion == "B":
        suma = 0
        for t in temps:
            suma += t
        print(f"El promedio semanal es: {suma / 7:.2f}°C")
    elif opcion == "C":
        max_temp = temps[0]
        for t in temps:
            if t > max_temp:
                max_temp = t
        print(f"La temperatura más alta fue de: {max_temp}°C")
    elif opcion == "D":
        print("Saliendo...")
    else:
        print("Opción no válida.")