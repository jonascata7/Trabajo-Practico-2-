asientos = [0] * 10
opcion = 0

while opcion != 3:
    print("\n--- CINE (10 ASIENTOS) ---")
    print("1. Ver asientos\n2. Vender entrada\n3. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        print("\nMapa de asientos:")
        for i in range(10):
            estado = "LIBRE" if asientos[i] == 0 else "OCUPADO"
            print(f"[ Asiento {i + 1}: {estado} ]", end=" ")
        print() 
        
    elif opcion == 2:
        asiento_elegido = int(input("Ingrese el número de asiento (1 a 10): "))
        if 1 <= asiento_elegido <= 10:
            indice = asiento_elegido - 1
            if asientos[indice] == 0:
                asientos[indice] = 1
                print("¡Vendido con éxito!")
            else:
                print("Asiento ocupado, elija otro.")
        else:
            print("Número de asiento no existe.")
            
    elif opcion == 3:
        print("Chau!")
    else:
        print("Opción inválida.")