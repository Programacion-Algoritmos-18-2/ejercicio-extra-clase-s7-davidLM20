from modelo.ordenamientoinsercion import * # se importa todos los elementos de modelado

valores = [10, 90, 1, 20, 4, 7, 9, 56, 87, 5] # se crea un arreglo con los valores

arreglo = OrdenamientoInsercion(valores) # se crea un objeto para realizar el ordenamiento
print("Arreglo desordenado:") # encabezado
print (valores, "\n") # imprime el arreglo desordenado

arreglo.ordenar(valores) # imprime el arreglo ordenado

