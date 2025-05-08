#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 

lista_range = list(range(1-1, 100, 4))

print(lista_range)


#2) 

mis_gatos = ["Nina", "Firu", "Negrita", "Pio", "Doffy"]

print(mis_gatos [-2])


#3)

mis_perros = [ ]
mis_perros.append("Camilo")
mis_perros.append("Paco")
mis_perros.append("Tobby")
print(mis_perros)


#4)

animales = ["perro", "gato", "conejo", "pez"]
animales [-3] = "loro"
animales [-1] = "oso"
print(animales)


#5) 

# RTA: Lo que hace este programa es lo siguiente, en la primer línea se crea la lista numeros
# asignandole los valores [8, 15, 3, 22, 7], en la segunda línea se utiliza max(numeros) para
#encontrar el número mayor, una vez que se obtiene el número (22) se usa numeros.remove(22)
#para eliminar el número 22 de la lista y en la última línea se imprime por pantalla la lista 
# modificada.


#6) 

lista_num = list(range(10, 30+1, 5))
rango_lista = lista_num[0:2]
print(rango_lista)


#7)

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "corsa"
autos[2] = "civic"
print(autos)


#8)

dobles = [ ]
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)


#9)

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)


#10)

lista_anidada = [15, "True", [25.5, 57.9, 30.6], "False"]

print(lista_anidada)