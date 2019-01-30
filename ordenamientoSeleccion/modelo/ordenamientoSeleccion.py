class OrdenamientoSeleccion: # se crea la clase principal

	def __init__(self, datos):# se crean los atributos globales de la clase
		self.datos = datos 

	def agregarInformacion(self, datos): # metodo para agregar la informacion 
		self.datos = datos

	def ordenar(self, datos): # metodo de ordenamiento, en este metodo se realiza todos los procesos para ordenar una estructura
		
		for i in range(len(self.datos)): # se recorrela estructura que contiene la informacion
			masPequenio = i # se inicializa una variable la cual tomara el valor de la cantidad mas pequeña del arreglo
			for j in range(i + 1, len(self.datos)): 
				if(self.datos[j] < self.datos[i]): # se compara la informacion de las dos variables para determinar cual es menor
					masPequenio = j # se da el valor de j 

			# se intercambia valores
			if masPequenio != i: # se compara si mas pequenio es diferente a i 
				temporal = self.datos[i] # se crea un auxiliar que tomael valor de la cantidad en i 
				self.datos[i] = self.datos[masPequenio] # datos en i toma el valor de mas pequenio
				self.datos[masPequenio] = temporal # y mas pequenio toma el valor del auxiliar
		# se imprimer el resultado
		print(self.__str__())

	#metodo str para devolver resultados
	def __str__(self):
		temporal = " " # se inicializa una cadena vacia

		for elemento in self.datos:
			temporal = "%s %s" % (temporal, elemento)

		temporal = "%s\n" % (temporal) 
		print("El arreglo ordenado es el siguiente:")

		return temporal # se retorna la cadena