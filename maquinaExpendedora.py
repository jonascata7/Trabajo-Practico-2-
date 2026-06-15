nombres = ["Papas Fritas", "Refresco", "Chocolate", "Alfajor", "Caramelos"]
precios = [1200, 1000, 1500, 800, 500]

print("--- MÁQUINA EXPENDEDORA ---")
for i in range(5):
    print(f"{i + 1}. {nombres[i]} (${precios[i]})")

eleccion = int(input("Ingrese el número del producto (1 a 5): "))

if 1 <= eleccion <= 5:
    indice = eleccion - 1
    print(f"Usted seleccionó: {nombres[indice]}")
    print(f"Total a pagar: ${precios[indice]}")
else:
    print("Código de producto inexistente.")