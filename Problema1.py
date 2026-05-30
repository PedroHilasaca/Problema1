import random

n = int(input("Ingrese el tamaño de la matriz (N x N): "))

matrix = []

print("\nGenerando matriz...\n")

for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(99, 999))
    matrix.append(row)


print("La matriz es:\n")

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


def convertir_lista(matriz):
    lista = []
    for fila in matriz:
        lista.extend(fila)
    return lista


def contar_multiplos(lista):

    if len(lista) == 1:
        numero = lista[0]

        if numero % 5 == 0 or numero % 7 == 0:
            return 1
        else:
            return 0

    mitad = len(lista) // 2

    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    return contar_multiplos(izquierda) + contar_multiplos(derecha)


# Llamar función
lista_numeros = convertir_lista(matrix)

resultado = contar_multiplos(lista_numeros)

print("\nCantidad de múltiplos de 5 o 7:", resultado)