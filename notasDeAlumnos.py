nombres = []
nota1 = []
nota2 = []
contador_alumnos = 0
opcion = 0

while opcion != 3:
    print("\n--- SISTEMA DE NOTAS ---")
    print("1. Registrar un nuevo alumno\n2. Mostrar lista completa y promedios\n3. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        if contador_alumnos < 10:
            nom = input("Nombre del alumno: ")
            n1 = float(input("Nota 1: "))
            n2 = float(input("Nota 2: "))
            
            nombres.append(nom)
            nota1.append(n1)
            nota2.append(n2)
            contador_alumnos += 1
            print("¡Alumno registrado!")
        else:
            print("Capacidad máxima alcanzada (10 alumnos).")
            
    elif opcion == 2:
        if contador_alumnos == 0:
            print("No hay alumnos registrados.")
        else:
            print("\nLista de Alumnos:")
            for i in range(contador_alumnos):
                promedio = (nota1[i] + nota2[i]) / 2
                print(f"{nombres[i]} - Promedio: {promedio}")
                
    elif opcion == 3:
        print("Saliendo...")
    else:
        print("Opción inválida.")