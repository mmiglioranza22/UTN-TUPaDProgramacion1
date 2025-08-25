# 1)

edad = int(input("Ingrese su edad: "))

if (edad > 18):
	print("Es mayor de edad")

# 2)

nota = int(input("Ingrese su nota: "))

if nota >= 6:
	print("Aprobado")
else:
	print("Desaprobado")

# 3)

numero = int(input("Ingrese un número par: "))

while True:
	if numero % 2 == 0:
		print("Ha ingresado un número par")
		break
	else:
		numero = int(input("Por favor intrese un número par: "))
	
# 4)

edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad < 12:
    print("Eres un niño.")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente.")
elif edad >= 18 and edad < 30:
    print("Eres un adulto joven.")
else:
    print("Eres un adulto.")

# 5) 

contraseña = input("Ingrese su contraseña: ")

minimo_8_caracteres = len(contraseña) >= 8
maximo_14_caracteres = len(contraseña) <= 14
  
if minimo_8_caracteres and maximo_14_caracteres :
 print("Ha ingresado una contraseña correcta.")
else:
 print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
sesgo_positivo = mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios)
sesgo_negativo = mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios)
sin_sesgo = mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios)

if sesgo_positivo:
	print("Sesgo positivo")
elif sesgo_negativo:
	print("Sesgo negativo")
else:
	print("Sin sesgo")


# 7)

frase = input("Ingrese una frase: ").strip()
frase_minuscula = frase.lower()

ultimo_caracter = len(frase) - 1
es_vocal = frase_minuscula[ultimo_caracter] == "a" or frase_minuscula[ultimo_caracter] == "e" or frase_minuscula[ultimo_caracter] == "i" or frase_minuscula[ultimo_caracter] == "o" or frase_minuscula[ultimo_caracter] == "u"

if es_vocal:
 print(f"{frase}!")
else:
 print(frase) 


# 8)

nombre = input("Ingrese su nombre: ")

opcion = int(input("Elija una opción:\n1 si quiere su nombre en mayúscula,\n2 si quiere su nombre en minúscula,\n3 si quiere la primera letra en mayúscula\n"))

if opcion == 1:
	print(nombre.upper())
elif opcion == 2:
	print(nombre.lower())
else:
	print(nombre.title())


# 9)

magnitud = int(input("Introduce tu edad: "))

if magnitud < 3:
  print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo.")
    
# 10)

hemisferio = input("Indique su hemisferio (N/S): ")
mes = input("Indique el mes del año: ")
dia = int(input("Indique el día: "))
dia_calendario = 0

enero = marzo = mayo = julio = agosto = octubre = 31
abril = junio = septiembre = noviembre = 30
febrero = 29 # El único margen de error es que este algoritmo no sabe cuantos dias tiene febrero, por lo que se asume 29. Se podría igualmente preguntar cuantos días tiene febrero al usuario y eso ajusta el margen de error.

if (dia > 31 or (mes == "febrero" and dia > 29) or ((mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre") and dia > 30)):
	print("La fecha es imposible. Adios.")
else:	
	# Se tiene que convertir el dia del mes en un dia calendario (entre los 365 dias) para usar como rango
	# ej: 1 de enero es el dia 1, 31 de diciembre es el dia 365
	# Se revisa el mes, y se le suman los días de los meses anteriores (a febrero se le suman los 31 días anteriores de enero, por lo que 1 de febrero es el día 32 del calendario)
	if (mes == "enero"):
		dia_calendario = dia 
	elif (mes == "febrero"):
		dia_calendario = dia + enero 
	elif (mes == "marzo"):
		dia_calendario = dia + enero + febrero 
	elif (mes == "abril"):
		dia_calendario = dia + enero + febrero + marzo 
	elif (mes == "mayo"):
		dia_calendario = dia + enero + febrero + marzo + abril 
	elif (mes == "junio"):
		dia_calendario = dia + enero + febrero + marzo + abril + mayo 
	elif (mes == "julio"):
		dia_calendario = dia + enero + febrero + marzo + abril + mayo + junio 
	elif (mes == "agosto"):
		dia_calendario = dia + enero + febrero + marzo + abril + mayo + junio + julio 
	elif (mes == "septiembre"):
		dia_calendario = dia + enero + febrero + marzo + abril + mayo + junio + julio + agosto 
	elif (mes == "octubre"):
		dia_calendario = dia + enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre 
	elif (mes == "noviembre"):
		dia_calendario = dia + enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre 
	elif (mes == "diciembre"):
		dia_calendario = dia + enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre

	if dia_calendario >= 356 or dia_calendario <= 80: # Desde el 21 de diciembre hasta el 20 de marzo (incluidos)
		if (hemisferio == "N"):
			print("Invierno")
		elif (hemisferio == "S"):
			print("Verano")
	elif 81 <= dia_calendario <= 172: # Desde el 21 de marzo hasta el 20 de junio (incluidos)
		if (hemisferio == "N"):
			print("Primavera")
		elif (hemisferio == "S"):
			print("Otoño")
	elif 173 <= dia_calendario <= 264: # Desde el 21 de junio hasta el 20 de septiembre (incluidos)
		if (hemisferio == "N"):
			print("Verano")
		elif (hemisferio == "S"):
			print("Invierno")
	elif 265 <= dia_calendario <= 355: # Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
		if (hemisferio == "N"):
			print("Otoño")
		elif (hemisferio == "S"):
			print("Primavera")