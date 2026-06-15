codigo_producto = [101, 102, 103, 104, 105]
nombre_producto = ["Remeras", "Pantalones", "Zapatillas", "Buzos", "Gorras"]
cantidad_stock = [10, 5, 0, 8, 12]

opcion = 0
while opcion != 4:
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Mostrar inventario\n2. Vender producto\n3. Reponer producto\n4. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        print("\nCÓDIGO | PRODUCTO | STOCK")
        for i in range(5):
            print(f"{codigo_producto[i]}    | {nombre_producto[i]} | {cantidad_stock[i]}")
            
    elif opcion == 2:
        cod_buscar = int(input("Ingrese el código del producto a vender: "))
        i = 0
        encontrado = False
        
        while i < 5 and not encontrado:
            if codigo_producto[i] == cod_buscar:
                encontrado = True
                posicion = i
            else:
                i += 1
                
        if encontrado:
            if cantidad_stock[posicion] > 0:
                cantidad_stock[posicion] -= 1
                print(f"Venta realizada. Nuevo stock de {nombre_producto[posicion]}: {cantidad_stock[posicion]}")
            else:
                print(f"Error: Sin stock disponible de {nombre_producto[posicion]}.")
        else:
            print("Código de producto no encontrado.")
            
    elif opcion == 3:
        cod_buscar = int(input("Ingrese el código del producto a reponer: "))
        i = 0
        encontrado = False
        
        while i < 5 and not encontrado:
            if codigo_producto[i] == cod_buscar:
                encontrado = True
                posicion = i
            else:
                i += 1
                
        if encontrado:
            print(f"Producto: {nombre_producto[posicion]}. Stock actual: {cantidad_stock[posicion]}")
            cant_reponer = int(input("Cantidad a sumar al stock: "))
            if cant_reponer > 0:
                cantidad_stock[posicion] += cant_reponer
                print("Stock actualizado con éxito.")
            else:
                print("Cantidad inválida.")
        else:
            print("Código de producto no encontrado.")
            
    elif opcion == 4:
        print("Saliendo del sistema de inventario.")
    else:
        print("Opción inválida.")