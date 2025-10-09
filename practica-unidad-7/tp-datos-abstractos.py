# 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 3200

print(precios_frutas)


# 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)


# 3

frutas = list(precios_frutas.keys())

print(frutas)


# 4

guia_telefonica = {}

while len(guia_telefonica) < 5:
	key = input("Ingrese el nombre del contacto: ")
	value = input("Ingrese el numero: ")
	guia_telefonica[key] = value

print(guia_telefonica)
contacto = input("Indique el contacto que desea consultar: ")

print(guia_telefonica[contacto])


# 5

frase = input("Ingrese una frase: ").strip()
lista_palabras = frase.split()
diccionario_palabras = {}

for palabra in lista_palabras:
	if (diccionario_palabras.get(palabra) == None):
		diccionario_palabras[palabra] = 1
	else:
		diccionario_palabras[palabra] = diccionario_palabras.get(palabra) + 1

print(f"Palabras únicas: {set(lista_palabras)}")
print(f"Recuento: {diccionario_palabras}")


# 6

alumnos = {}

while len(alumnos.keys()) < 3:
	alumno = input("Ingrese un alumno: ")
	notas = []
	for i in range(3):
		nota = int(input("Ingrese una nota para ese alumno: "))
		notas.append(nota)
	
	alumnos[alumno] = tuple(notas)

print(alumnos)

for alumno in alumnos:
	promedio = 0
	for nota in alumnos[alumno]:
		promedio += nota

	print(f"Promedio de {alumno}: {round(promedio / 3, 1)}")

# 8

productos = {
	"Coca-Cola": 50,
	"Fideos": 100,
	"Latas de atun": 40,
	"Latas de arvejas": 0
}

print(productos)

producto = input("Consulte un producto: ")
if producto in productos:
	print(f"El stock para {producto} es {productos[producto]} unidades")
else:
	print("Producto inexistente")

producto = input("Agregue una unidad a un producto: ")

if producto in productos:
	productos[producto] = productos[producto] + 1
else:
	productos[producto] = 1

print(productos)

# 9

agenda = {
	("lunes", "10:00"): "Meet",
	("martes", "11:00"): "Call con accionistas",
	("jueves", "10:00"): "Medico",
	("jueves", "14:00"): "Dentista"
}

print(agenda)

dia = input("Ingrese el día de consulta: ")
hora = input("Ingrese la hora: ")

fecha = (dia, hora)

if fecha in agenda:
	print(f"{fecha}: {agenda[fecha]}")
else:
	print("No hay eventos para el día y hora indicados.")

# 10

original = {"Argentina" : "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for pais in original:
	ciudad = original[pais]
	invertido[ciudad] = pais

print(invertido)
