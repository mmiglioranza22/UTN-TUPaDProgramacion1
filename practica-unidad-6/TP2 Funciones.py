# 1

def imprimir_hola_mundo():
	print("Hola Mundo!")

imprimir_hola_mundo()

# 2

def saludar_usuario(nombre):
	print(f"Hola {nombre}!")

saludar_usuario(input("Ingrese su nombre: "))

# 3

def informacion_personal(nombre, apellido, edad, residencia):
	print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su edad: "), input("Ingrese su residencia: "))

# 4

import math

def calcular_area_circulo(radio):
	return round(math.pi * radio ** 2, 2)

def calcular_perimetro_circulo(radio):
	return round(2 * math.pi * radio, 2)

radio = int(input("Ingrese el radio del círculo: "))

print(f"El área del circulo es: {calcular_area_circulo(radio)}")
print(f"La circunferencia del circulo es: {calcular_perimetro_circulo(radio)}")


# 5

def segundos_a_horas(segundos):
	return segundos / 60 / 60

print(segundos_a_horas(int(input("Ingrese una cantidad de segundos: "))))

# 6

def tabla_multiplicar(numero):
	for i in range(0, 11):
		print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(int(input("Ingrese un numero: ")))


# 7

def operaciones_basicas(a, b):
	multiplicacion = a * b
	division = a / b
	suma = a + b
	resta = a - b

	return (f"{a} x {b} = {multiplicacion}", f"{a} / {b} = {division}", f"{a} + {b} = {suma}", f"{a} - {b} = {resta}")

print(operaciones_basicas(int(input("Ingrese un numero: ")), int(input("Ingrese otro numero: "))))


# 8

def calcular_imc(peso, altura):

	return round(peso / (altura ** 2), 2)

print(calcular_imc(int(input("Ingrese su peso en kilos: ")), float(input("Ingrese su altura en metros: "))))
	

# 9

def celsius_a_fahrenheit(celsius):
	return (celsius * 9/5) + 32


print(f"{round(celsius_a_fahrenheit(float(input("Ingrese una temperatura en celsius: "))), 2)}")


# 10

def calcular_promedio(a, b, c):
	return (a + b + c) / 3

print(f"Promedio: {calcular_promedio(int(input("Ingrese un numero: ")), int(input("Ingrese otro numero: ")), int(input("Ingrese el último numero: ")))}")