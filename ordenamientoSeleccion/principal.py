from modelo.ordenamientoSeleccion import * # se importa toda la informaciondel paquete modelo


valores = [4,3,1,9,8,7] # se crea el arreglo con los valores 

arreglo = OrdenamientoSeleccion(valores) # se crea un objeto tipo OrdenamientoSeleccion y se le da el parametro en este caso valores
print("El arreglo en desorden es:") # encabezado
print(valores) # se imprimer el arreglo en desorden
arreglo.ordenar(valores) # se llama el metodo ordenar

