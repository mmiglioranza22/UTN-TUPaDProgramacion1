# 1

for i in range(1, 101):
	print(i)


# 2

num = int(input("Ingrese un número entero: "))
original = num
digitos = 0

if num == 0:
	digitos = 1
else:
	while num != 0:
			num //= 10
			digitos += 1

	
print(f"El número {original} tiene {digitos} digitos")


# 3

num_1 = int(input("Ingrese un valor: "))
num_2 = int(input("Ingrese otro valor: "))
suma = 0

for i in range(num_1 + 1, num_2):
	suma += i

print(f"La suma de digitos entre {num_1} y {num_2} (excluidos) es {suma}")


# 4

numero = int(input("Ingrese un número: (0 para salir del programa): "))
suma = 0

while (numero != 0):
	suma += numero
	numero = int(input("Ingrese un número: (0 para salir del programa): "))

print(f"La suma de los numero ingresados es {suma}")	


# 5

import random

acierto = random.randint(0,9)
intentos = 0

adivinanza = int(input("Ingrese un número entre 0 y 9: "))

while True:
	if adivinanza < 0 or adivinanza > 9:
		adivinanza = int(input("Fuera de rango. Ingrese un número entre 0 y 9: "))
	else:
		intentos += 1
		if adivinanza == acierto:
			if intentos == 1:
				print("Adivinaste! Lo hiciste en el primer intento")
				break
			else:
				print(f"Adivinaste! Lo hiciste en {intentos} intentos")
				break
		else:
			adivinanza = int(input("Ese no era. Intenta otro número entre 0 y 9: "))
	

# 6 

for i in range(100, 0, -1):
	if i % 2 == 0:
		print(i)


# 7

num = int(input("Ingrese un número: "))
suma = 0

for i in range(0, num + 1):
	suma += i

print(f'La suma de los numeros entre 0 y {num} (inclusive) es {suma}')


# 8

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(0, 100):
	num = int(input("Ingrese un número: "))
	if num % 2 == 0:
		pares += 1
	else:
		impares += 1
	
	if num > 0:
		positivos += 1
	else:
		negativos += 1

print(f"Pares: {pares}. Impares: {impares}. Positivos: {positivos}. Negativos: {negativos}")


# 9

sum = 0

for i in range(0, 100):
	num = int(input("Ingrese un número: "))
	sum += num

print(f"Suma total: {sum}. Media: {sum / 10}")

# 10

num = int(input("Ingrese un numero: "))

# Obtener los digitos del numero
digitos = len(str(num))
inverso = 0

while num != 0:
	# Obtener la posicion (indexada a 0)
	posicion = digitos - 1

	# El valor es el resto del numero con 10 (el último dígito) multiplicado por 10 elevado a la posición respectiva (esto da la centena, decena, unidad inversa)
	valor = int((num % 10) * (10 ** posicion))
	inverso = inverso + valor
	
	# División entera del numero para ir descartando los valores que ya usamos para la inversión (no me interesan los decimales)
	num //= 10

	digitos -= 1

print(inverso)