"""EJERCICIO 1"""

# Función recursiva para calcular el factorial
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Función que muestra los factoriales desde 1 hasta y
def factorial_de_todo(y):
    for i in range(1, y + 1):
        resultado = factorial_recursivo(i)
        print(f"{i}! = {resultado}")

# Programa principal
y = int(input("Ingrese un número entero positivo: "))
print(f"Resultado del factorial de los números del 1 al {y}:")

if y < 1:
    print("Por favor, ingrese un número mayor o igual a 1.")
else:
    factorial_de_todo(y)


"""EJERCICIO 2"""   

# Función recursiva para calcular la serie de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Programa principal
# Pedir posición al usuario
pos = int(input("\nPor favor, ingrese la posición hasta donde quiere ver la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {pos}:")
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")

"""EJERCICIO 3"""

# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal
base = int(input("Por favor, ingrese la base: "))
exponente = int(input("Por favor, ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"\n{base} elevado a la {exponente} es: {resultado}")

"""EJERCICIO 4"""

# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
# Pedir número al usuario
numero = int(input("Por favor, ingrese un número entero positivo para convertir a binario: "))

#Caso especial 0
if numero == 0:
    binario = "0"
else:
    binario = decimal_a_binario(numero)

print(f"\nEl número {numero} en binario es: {binario}")

"""EJERCICIO 5"""

# Función recursiva para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y última letra no son iguales, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva
    return es_palindromo(palabra[1:-1])

# Programa principal
entrada = input("Por favor, ingrese una palabra (sin espacios ni tildes): ")

if es_palindromo(entrada):
    print(f"La palabra '{entrada}' es un palíndromo.")
else:
    print(f"La palabra '{entrada}' NO es un palíndromo.")

"""EJERCICIO 6"""  

# Función recursiva para sumar los dígitos de un número
def suma(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma(n // 10)

# Programa principal con input
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    resultado = suma(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

"""EJERCICIO 7"""

# Función recursiva para contar los bloques de una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Programa principal 
bloques = int(input("Ingrese el número de bloques en el nivel más bajo: "))

if bloques < 1:
    print("Por favor, ingrese un número entero positivo mayor o igual a 1.")
else:
    total = contar_bloques(bloques)
    print(f"El total de bloques para construir la pirámide es: {total}")

"""EJERCICIO 8"""


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        contador = 1 if numero % 10 == digito else 0
        return contador + contar_digito(numero // 10, digito)

# Programa principal con input
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar (0-9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Por favor, ingrese valores válidos: número positivo y dígito entre 0 y 9.")
else:
    total = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {total} veces en {numero}.")