"""Ejercicio 1"""
# Se crea una lista con los múltiplos de 4 del 1 al 100
lista_multiplos_4 = list(range(4, 101, 4))
print(lista_multiplos_4)


"""Ejercicio 2"""
# El programa crea una lista con varios elementos 
mi_lista = ["gatos", "pizza", "helado", "sushi", "tacos"]
print("Penúltimo elemento:", mi_lista[-2])


"""Ejercicio 3"""
lista_vacia = []

# Agregar tres palabras
lista_vacia.append("libro")
lista_vacia.append("sol")
lista_vacia.append("montaña")

# Imprimir la lista resultante
print(lista_vacia)


"""Ejercicio 4"""
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo elemento
animales[1] = "loro"
# Reemplazar el último elemento
animales[-1] = "oso"

# Imprimir la lista resultante
print(animales)


"""Ejercicio 5"""
#El programa elimina el número más grande de la lista y muestra la lista resultante.


"""Ejercicio 6"""
numeros = list(range(10, 31, 5))
print("Lista completa:", numeros)
print("Dos primeros:", numeros[:2])


"""Ejercicio 7"""
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores en los índices 1 y 2
autos[1] = "mustang"
autos[2] = "civic"

# Mostrar la lista actualizada
print(autos)


"""Ejercicio 8"""
dobles = []

# Agregar el doble de 5, 10 y 15 usando append directamente
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print(dobles)


"""Ejercicio 9"""
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" 
compras[1][1] = "tallarines"

# c) Eliminar "pan"
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)


"""Ejercicio 10"""
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)
