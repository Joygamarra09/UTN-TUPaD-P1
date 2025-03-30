#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 

nombre = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados.

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = input("Por favor ingrese su edad: ")
recidencia = input("Por favor ingrese su lugar de recidencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {recidencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = input("Ingrese el radio del círculo: ")
radio = int(radio)
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"Según el dato ingresado el área del circulo es {area} y el perímetro es {perimetro}.")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = input("Por favor ingrese la cantidad de segundos que desea pasar a horas: ")
segundos = int(segundos)
horas = segundos / 3600
print(f"Los segundos ingresados equivalen {horas} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = input("Ingrese un número entero: ")
numero = int(numero)
print(f"La tabla del número {numero} es: ")
print(f"{numero} x 1 = ", numero * 1)
print(f"{numero} x 2 = ", numero * 2)
print(f"{numero} x 3 = ", numero * 3)
print(f"{numero} x 4 = ", numero * 4)
print(f"{numero} x 5 = ", numero * 5)
print(f"{numero} x 6 = ", numero * 6)
print(f"{numero} x 7 = ", numero * 7)
print(f"{numero} x 8 = ", numero * 8)
print(f"{numero} x 9 = ", numero * 9)
print(f"{numero} x 10 = ", numero * 10)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = input("Ingrese el primer número entero, éste debe ser distinto a 0: ")
num2 = input("Ingrese el segundo número entero, éste debe ser distinto a 0: ")
num1 = int(num1)
num2 = int(num2)
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
division = num1 / num2
print(f"El resultado de la suma entre {num1} y {num2} es: {suma}")
print(f"El resultado de la resta entre {num1} y {num2} es: {resta}")
print(f"El resultado de la multiplicación entre {num1} y {num2} es: {multi}")
print(f"El resultado de la división entre {num1} y {num2} es: {division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.

peso = input("Por favor ingrese su peso en kg: ")
altura = input("Por favor ingrese su altura en metros: ")
peso = float(peso)
altura = float(altura)
IMC = peso / (altura ** 2)
print(f"Según los datos ingresados su Índice de Masa Corporal es: {IMC}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.

grados_celcius = input("Ingrese una temperatura en grados Celcius: ")
grados_celcius = int(grados_celcius)
grados_fahren = (grados_celcius * 1.8) + 32
print(f"El equivalente en Fahrenheit de la temperatura ingresada es: {grados_fahren}℉")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
num3 = input("Ingrese el tercer número: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números ingresados es: {promedio}")