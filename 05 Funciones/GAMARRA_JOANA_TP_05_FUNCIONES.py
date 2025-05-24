#1)

#Definición de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()   #Se llama a la función imprimir_hola_mundo.

#2)

#Definición de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#Programa principal
nombre = input("Por favor, ingrese su nombre: ")   #Se define la variable nombre a través de un input.
saludar_usuario(nombre)  #Se llama a la función saludar_usuario().

#3)

#Definición de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Programa principal

#Definición de variables.
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = int(input("Por favor, ingrese su edad: "))
residencia = input("Por favor, ingrese su lugar de residencia: ")

#Llamado a la función informacion_personal().
informacion_personal(nombre, apellido, edad, residencia)

#4)

#Definición de funciones.
import math

def calcular_area_circulo(radio):
    return math.pi * (radio * radio)
    

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


#Programa principal.

#Se define la variable radio a través de un input.
radio = float(input("Por favor, ingrese el radio de un círculo: "))

resultado_area = calcular_area_circulo(radio)
resultado_perimetro = calcular_perimetro_circulo(radio)

#Se muestra el resultado al usuario.
print(f"El área del círculo es {resultado_area}")
print(f"El perímetro del círculo es {resultado_perimetro}")

#5)

#Definición de funciones
def segundos_a_horas(segundos):
    return segundos / 3600
   

#Programa principal
#Se define la variable segundos a través de un input.
segundos = int(input("Por favor, ingrese los segunos que desea pasar a horas: "))

#Se define la variable horas.
horas = segundos_a_horas(segundos)

#Se muestra el resultado al usuario.
print(f"Los segundos ingresados equivalen a", round(horas, 2), " horas." )

#6)

#Definición de funciones.
def tabla_multiplicar(num):
    for i in range(1, 10 + 1):
        print(f"{num} x {i} = ", num * i)

#Programa principal.
#Se define la variable a través de un input.
num = int(input("Por favor, ingrese un número del cual desee conocer su tabla de multiplicar: "))

#Llamado a la función.
tabla_multiplicar(num)

#7)

#Definición de funciones.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Se evita división por cero.
    while b == 0:
        b = int(input("No se puede dividir por cero. Por favor, vuelva a intentarlo: "))
    
    division = a / b

    return (suma, resta, multiplicacion, division)


#Programa principal.
#Se define las variables a través de un input.
a = int(input("Por favor, ingrese un número: "))
b = int(input("Por favor, ingrese un segundo número: "))

resultados = operaciones_basicas(a, b)
#Se muestra al usuario el resultado.
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print("División: ", round(resultados[3], 2))

#8)

#Definición de funciones.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#Programa principal.
#Se definen las variables a través de un input.
peso = float(input("Por favor, ingrese su peso: "))
altura = float(input("Por favor, ingrese su altura: "))

imc = calcular_imc(peso, altura)

#Se muestra el resultado al usuario.
print(f"Tu IMC es: {round(imc, 2)}")

#9)

#Definición de funciones.
def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32

#Programa principal.
#Se define la variable a través de un input.
celsius = int(input("Por favor, ingrese la temperatura en Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

#Mostramos los grados en fahrenheit.
print(f"El equivalente en fahrenheit de los grados ingresados es: {fahrenheit}")

#10)

#Definición de funciones.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal.
#Se definen las variables a través de input.
a = int(input("Por favor ingrese el primer número: "))
b = int(input("Por favor ingrese el segundo número: "))
c = int(input("Por favor ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)

#Mostramos al usuario el promedio.
print(f"El promedio de los números ingresados es: {round(promedio, 2)}")