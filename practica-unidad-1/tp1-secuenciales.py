# 1
print("Hola Mundo!")

# 2
nombreUsuario = input("Por favor ingrese su nombre: ")
print(f"Hola {nombreUsuario}!")

# 3
nombreUsuario = input("Por favor ingrese su nombre: ")
apellidoUsuario = input("Por favor ingrese su apellido: ")
edadUsuario = input("Por favor ingrese su edad: ")
domicilioUsuario = input("Por favor ingrese su lugar de residencia: ")

print(f"Soy {nombreUsuario} {apellidoUsuario}, tengo {edadUsuario} años y vivo en {domicilioUsuario}")

# 4
import math

radioCirculo = int(input("Ingrese el radio del círculo: "))
areaCirculo = math.pi * math.pow(radioCirculo, 2)
perimetroCirculo = 2 * math.pi * radioCirculo

print(f"Área: {areaCirculo}. Perímetro: {perimetroCirculo}")

# 5

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 60 / 60

print(f"{segundos} segundos equivalen a {horas} horas")

# 6

numero = int(input("Ingrese un numero: "))

for i in range(1,11):
	print(f"{i} x {numero} = {i * numero}")

# 7

primerNumero = int(input("Ingrese un numero entero distinto de cero: "))
segundoNumero = int(input("Ingrese un otro numero entero distinto de cero: "))

if (primerNumero == 0 or segundoNumero == 0):
	print("Los números son inválidos")
else:
	print(f"Suma: {primerNumero + segundoNumero} \nResta: {primerNumero - segundoNumero} \nMultiplicación: {primerNumero * segundoNumero} \nDivisión: {primerNumero / segundoNumero} ")
	
# 8
altura = float(input("Ingrese un su altura en metros: "))
peso = float(input("Ingrese un su peso en kilos: "))

print(f"Su IMC (índice de masa corporal) es: {peso / (altura ** 2)}")

# 9
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = ((9/5) * celsius) + 32

print("La temperatura en Fharenheit es: " + str(fahrenheit))

# 10

primerNumero = int(input("Ingrese un numero: "))
segundoNumero = int(input("Ingrese otro numero: "))
tercerNumero = int(input("Ingrese otro numero: "))

promedio = (primerNumero + segundoNumero + tercerNumero) / 3

print(f"El promedio de los numeros ingresados es: {str(promedio)}")