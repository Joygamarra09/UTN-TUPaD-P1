"""Ejercicio 1:"""

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el diccionario actualizado
print(precios_frutas)


"""Ejercicio 2:"""

# Diccionario existente (luego de agregar las frutas)
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualizar los precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario actualizado
print(precios_frutas)

"""Ejercicio 3:"""

# Diccionario actualizado
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Crear una lista con solo las frutas
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista
print(lista_frutas)

"""Ejercicio 4:"""

# Crear diccionario vacío para guardar los contactos
agenda = {}

# Cargar 5 contactos
print("Cargá 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i + 1}: ")
    numero = input(f"Ingresá el número de teléfono de {nombre}: ")
    agenda[nombre] = numero

# Consultar un contacto
consulta = input("¿De qué persona querés saber el número?: ")

if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontró un contacto con el nombre: {consulta}")


"""Ejercicio 5:"""

# Pedir frase al usuario
frase = input("Ingresá una frase: ")

# Convertir la frase en una lista de palabras
palabras = frase.split()

# Crear un set con las palabras únicas
palabras_unicas = set(palabras)

# Contar cuántas veces aparece cada palabra
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Mostrar resultados
print("Palabras únicas:")
print(palabras_unicas)

print("Cantidad de veces que aparece cada palabra:")
for palabra, cantidad in contador_palabras.items():
    print(f"{palabra}: {cantidad}")


"""Ejercicio 6:"""

# Crear diccionario para guardar alumnos y sus notas
notas_alumnos = {}

# Ingresar datos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    print(f"Ingresá 3 notas para {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    notas_alumnos[nombre] = (nota1, nota2, nota3)

# Mostrar promedios
print("Promedios de los alumnos:")
for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / 3
    print(f"{alumno}: {promedio:.2f}")

"""Ejercicio 7:"""

# Sets de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "Pedro", "María", "Sofía"}
parcial2 = {"Luis", "María", "Carlos", "Valentina", "Sofía"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos parciales:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

"""Ejercicio 8:"""

# Diccionario inicial de productos y stock
stock_productos = {
    "Arroz": 20,
    "Fideos": 15,
    "Harina": 10
}

# Mostrar los productos disponibles
print("Productos disponibles:", list(stock_productos.keys()))

# Consultar un producto
producto = input("Ingresá el nombre del producto que querés consultar o actualizar: ")

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")

    # Agregar unidades
    try:
        cantidad = int(input(f"¿Cuántas unidades querés agregar al stock de {producto}?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
    except ValueError:
        print("Por favor, ingresá un número válido.")
else:
    # Producto nuevo
    try:
        nuevo_stock = int(input(f"{producto} no está en el sistema. ¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] = nuevo_stock
        print(f"{producto} fue agregado con un stock de {nuevo_stock} unidades.")
    except ValueError:
        print("Por favor, ingresá un número válido.")

# Mostrar el stock final
print("Stock actualizado:")
for prod, stock in stock_productos.items():
    print(f"{prod}: {stock} unidades")

"""Ejercicio 9:"""

# Crear la agenda como diccionario
agenda = {}

# Cargar eventos
print("Cargá eventos en la agenda.")
for i in range(3):  # Podés cambiar el 3 por más eventos si querés
    dia = input(f"Ingresá el día del evento {i + 1} (por ejemplo: 'Lunes'): ")
    hora = input("Ingresá la hora (por ejemplo: '14:00'): ")
    evento = input("Descripción del evento: ")

    clave = (dia.lower(), hora)
    agenda[clave] = evento

# Consultar un evento
print(" Consultar actividad en un día y hora específicos.")
consulta_dia = input("Ingresá el día que querés consultar: ").lower()
consulta_hora = input("Ingresá la hora (por ejemplo: '14:00'): ")

clave_consulta = (consulta_dia, consulta_hora)

if clave_consulta in agenda:
    print(f" Hay un evento el {consulta_dia.capitalize()} a las {consulta_hora}: {agenda[clave_consulta]}")
else:
    print(f" No hay ningún evento registrado el {consulta_dia.capitalize()} a las {consulta_hora}.")


"""Ejercicio 10:"""

# Diccionario original: país -> capital
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Invertir el diccionario: capital -> país
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el resultado
print(capitales_paises)


