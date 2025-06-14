"""EJERCICIO 1"""

# Función recursiva para calcular el factorial
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + factorial_recursivo(n - 1)

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

