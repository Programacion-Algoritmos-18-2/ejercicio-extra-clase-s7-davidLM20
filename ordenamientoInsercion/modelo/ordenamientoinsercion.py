class OrdenamientoInsercion(): # se crea la clase principal

    def __init__(self, datos): # se crea los atributos globales
        self.datos = datos 

    def agregarInformacion(self, datos): # metodo para agregar la informacion
        self.datos = datos

    def ordenar(self,datos): # metodo de ordenamiento, en este metodo se realiza todos los procesos para ordenar una estructura
        insecion = 0  #variable temporal para contener el elemento a insertar
        for i in range(1, len(self.datos)): #itera a traves de datos - 1 elementos
            insercion = self.datos[i] # almacena el valor en el elemento actual
            posicion = i # inicializa ubicacion para colocar el elemento

            while posicion > 0 and self.datos[posicion - 1] > insercion: # busca un lugar para colocar el elemento actual
                self.datos[posicion] = self.datos[posicion - 1] # desplaza el elemento una posicion a la derecha
                posicion = posicion - 1 

            self.datos[posicion] = insercion # coloca el elemento insertado

            print(self.__str__()) #imprime la pasada del algoritmo
        print("El arreglo ordenado es el siguiente:\n") # encabezado
        print(self.__str__()) # imprime la pasada final del algoritmo


    def imprimirPasada(self, pasada, indice): # imprime una pasada del algoritmo
        print("despues de pasada %2d:", pasada)

        for i in range (0,indice):    # mprime los elementos hasta el elemento intercambiado
            print(self.datos[i] + " ")

        print(self.datos[i] + "* ") # indica intercambio

        for i in range(indice + 1, len(self.datos)): # ermina de imprimir el arreglo en pantalla
            print(self.datos[i] + " ")
        print("") # para alineacion
        
        for i in range(0, pasada): # indica la cantidad del arreglo que este ordenado
            print("--------------")
        print(" ")

    
    #metodo str para devolver resultados`
    def __str__(self):
        temporal = " " # se inicializa una cadena vacia

        for elemento in self.datos: # itera a traves del arreglo
            temporal = "%s %s" % (temporal, elemento)

        temporal = "%s%s\n" % (temporal, "\n") 

        return temporal # se retorna la cadena