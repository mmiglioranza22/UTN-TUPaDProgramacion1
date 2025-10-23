# 1

def factorial(num):
	if num == 0:
		return 1 # por convención matemática el factorial de 0 es 1
	else:
		return num * factorial(num - 1)
	

numero = int(input("Ingrese un número: "))

print(f"El factorial de {numero} es {factorial(numero)}")

# 2

def fibonacci(num):
	if num <= 0:
		raise ValueError("El numero no puede ser menor o igual a 0")
	elif num == 1:
		return 0
	elif num == 2:
		return 1
	else:
		return fibonacci(num-1) + fibonacci(num-2)
	
numero = int(input("Ingrese un número: "))

for i in range(1, numero):
	print(f"{fibonacci(i)} ")	


# 3

def potencia_recursiva(base, potencia):
	if base == 0:
		return 0
	elif potencia == 0:
		return 1
	else:
		return base * potencia_recursiva(base, potencia - 1)


base = int(input("Ingrese un número (base): "))
potencia = int(input("Ingrese un número (potencia): "))

print(potencia_recursiva(base, potencia))

# 4

def binario(decimal):
	if decimal == 0:
		return "0"
	elif decimal == 1:
		return "1"
	else:
		cociente = decimal // 2 # el cociente tiene que seguir dividiéndose para avanzar el algoritmo, va a ser el primer dígito cuando finalice
		resto = decimal % 2 # el resto es lo que determina si ese numero debe tener un 1 o un 0 en su último dígito en representación binaria
		return binario(cociente) + str(resto)

decimal = int(input("Ingrese un decimal: "))

print(binario(decimal))

# 5

def es_palindromo(cadena):
	if len(cadena) <= 1:
		return True 
	if cadena[0] == cadena[-1]:
		return es_palindromo(cadena[1:-1]) # hacer el chequeo eliminando las puntas de la cadena hasta llegar a 1 (pivote de la cadena) o 0 (palabra con numero par de caracteres)
	else:
		return False

cadena = input("Ingrese una palabra: ")

print(f"La palabra es un palíndromo: {es_palindromo(cadena)}")

# 6

def suma_digitos(n):
	ultimo_digito = n % 10
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return ultimo_digito + suma_digitos(n//10)
	

numero = int(input("Ingrese un numero: "))

print(suma_digitos(numero))

# 7

def contar_bloques(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return n + contar_bloques(n - 1)
	

numero = int(input("Ingrese un numero: "))

print(contar_bloques(numero))


