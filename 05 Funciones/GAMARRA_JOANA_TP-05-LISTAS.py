#1) 

#Se crea una lista con la función range().
lista_range = list(range(1-1, 100, 4))

#Se imprime por pantalla la lista creada anteriormente.
print(lista_range)


#2) 

#Se crea una lista con cinco elementos.
mis_gatos = ["Nina", "Firu", "Negrita", "Pio", "Doffy"]

#Se imprime por pantalla el penúltimo elemento utilizando el indexing con números negativos.
print(mis_gatos [-2])


#3)

#Se crea una lista vacía.
mis_perros = [ ]

#Se agregaron tres palabras con append
mis_perros.append("Camilo")
mis_perros.append("Paco")
mis_perros.append("Tobby")

#Mostramos por pantalla la lista.
print(mis_perros)


#4)

#Creamos la lista animales con cuatro elementos.
animales = ["perro", "gato", "conejo", "pez"]

#Reemplazamos el segundo y último valor con las palabras "loro" y "oso",
#se utiliza el indexing con números negativos!
animales [-3] = "loro"
animales [-1] = "oso"

#Mostramso por pantalla la lista.
print(animales)


#5) 

# RTA: Lo que hace este programa es lo siguiente, en la primer línea se crea la lista numeros
# asignandole los valores [8, 15, 3, 22, 7], en la segunda línea se utiliza max(numeros) para
#encontrar el número mayor, una vez que se obtiene el número (22) se usa numeros.remove(22)
#para eliminar el número 22 de la lista y en la última línea se imprime por pantalla la lista 
# modificada.


#6) 

#Creamos una lista con la función range.
lista_num = list(range(10, 30+1, 5))
rango_lista = lista_num[0:2]

#Se muestra por pantalla la lista.
print(rango_lista)


#7)

#Se crea la lista autos.
autos = ["sedan", "polo", "suran", "gol"]

#Se reemplazan los valores centrales (índice 1 y 2)
autos[1] = "corsa"
autos[2] = "civic"

#Mostramos por pantalla la lista "autos".
print(autos)


#8)

#Creamos una lista vacía llamada dobles.
dobles = [ ]

#Agregamos el doble de 5, 10 y 15 usando append().
dobles.append(10)
dobles.append(20)
dobles.append(30)

#Mostramos por pantalla la lista dobles.
print(dobles)


#9)

#Creamos la lista compras.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

#Agregamos "jugo" usando append().
compras[2].append("jugo")

#Reemplazamos "fideos" por "tallarines".
compras[1][1] = "tallarines"

#Eliminamos "pan" de la lista del primer cliente
compras[0].remove("pan")

#Implimimos por pantalla la lista compras
print(compras)


#10)

#Creamos una lista con cuatro elementos y uno de ellos va a ser una lista anidada.
lista_anidada = [15, "True", [25.5, 57.9, 30.6], "False"]

#Se muestra por pantalla la lista.
print(lista_anidada)