"""Ejercicio 1: análisis de una matriz de ventas.

Representa las ventas de tres vendedores durante cuatro semanas usando
listas anidadas, ciclos for y acumuladores. No requiere librerías externas.
"""


def mostrar_matriz(matriz):
    """Muestra las ventas indicando vendedor y semana."""
    print("\nMATRIZ DE VENTAS (millones de pesos)")
    for i, fila in enumerate(matriz):
        print(f"Vendedor {i + 1}: ", end="")
        for j, venta in enumerate(fila):
            print(f"Semana {j + 1}: {venta:.2f}", end="  ")
        print()


def calcular_totales_vendedores(matriz):
    """Calcula y devuelve el total de ventas de cada vendedor."""
    totales = []
    for fila in matriz:
        total = 0
        for venta in fila:
            total += venta
        totales.append(total)
    return totales


def calcular_totales_semanas(matriz):
    """Calcula y devuelve el total de ventas de cada semana."""
    totales = []
    numero_semanas = len(matriz[0])

    for columna in range(numero_semanas):
        total = 0
        for fila in range(len(matriz)):
            total += matriz[fila][columna]
        totales.append(total)
    return totales


def mostrar_analisis(matriz):
    """Muestra todos los resultados calculados a partir de la matriz."""
    mostrar_matriz(matriz)

    totales_vendedores = calcular_totales_vendedores(matriz)
    print("\nTOTAL DE VENTAS POR VENDEDOR")
    for i, total in enumerate(totales_vendedores):
        print(f"Vendedor {i + 1}: {total:.2f} millones de pesos")

    totales_semanas = calcular_totales_semanas(matriz)
    print("\nTOTAL DE VENTAS POR SEMANA")
    for i, total in enumerate(totales_semanas):
        print(f"Semana {i + 1}: {total:.2f} millones de pesos")

    mayor_total = max(totales_vendedores)
    print("\nVENDEDOR CON MAYOR TOTAL")
    for i, total in enumerate(totales_vendedores):
        if total == mayor_total:
            print(f"Vendedor {i + 1}, con {total:.2f} millones de pesos")

    mayor_semana = max(totales_semanas)
    print("\nSEMANA CON MAYOR VOLUMEN DE VENTAS")
    for i, total in enumerate(totales_semanas):
        if total == mayor_semana:
            print(f"Semana {i + 1}, con {total:.2f} millones de pesos")

    suma_general = 0
    cantidad_ventas = 0
    for fila in matriz:
        for venta in fila:
            suma_general += venta
            cantidad_ventas += 1

    promedio = suma_general / cantidad_ventas
    print(f"\nPromedio general de ventas: {promedio:.2f} millones de pesos")
    print(f"Total general de ventas: {suma_general:.2f} millones de pesos")


def leer_entero(mensaje, minimo, maximo):
    """Solicita un entero dentro de un rango válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Ingrese un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero.")


def leer_venta(mensaje):
    """Solicita una venta numérica no negativa."""
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
            if valor >= 0:
                return valor
            print("La venta no puede ser negativa.")
        except ValueError:
            print("Entrada no valida. Ingrese un valor numerico.")


def main():
    # Cada fila representa un vendedor y cada columna una semana.
    ventas = [
        [12, 15, 10, 18],
        [8, 14, 16, 12],
        [20, 18, 15, 22]
    ]

    print("========== EJERCICIO 1: MATRIZ DE VENTAS ==========")
    print("ANÁLISIS INICIAL")
    mostrar_analisis(ventas)

    print("\n========== MODIFICAR UNA VENTA ==========")
    vendedor = leer_entero("Ingrese el número del vendedor (1, 2 o 3): ", 1, len(ventas))
    semana = leer_entero("Ingrese el número de la semana (1, 2, 3 o 4): ", 1, len(ventas[0]))
    nueva_venta = leer_venta("Ingrese el nuevo valor de la venta (millones de pesos): ")

    ventas[vendedor - 1][semana - 1] = nueva_venta

    print("\nVenta actualizada correctamente.")
    print("ANÁLISIS ACTUALIZADO")
    mostrar_analisis(ventas)


if __name__ == "__main__":
    main()
