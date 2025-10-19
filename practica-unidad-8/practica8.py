def leer_archivo():
	with open("productos.txt", "r") as archivo:
		productos = archivo.readlines()
		for linea in productos:
			producto = linea.strip().split(",")
			print(f"Producto: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}")

leer_archivo()

def agregar_producto():
	nuevo_producto = input("Ingrese un nuevo producto (nombre,precio,cantidad): ")
	producto = nuevo_producto.split(",")
	if len(producto) != 3:
		print("Formato incorrecto")
	else:
		with open("productos.txt", "a") as archivo:
			archivo.write(nuevo_producto + "\n")
		print("Producto ingresado")

agregar_producto()

def generar_diccionario_productos():
	lista = []
	with open("productos.txt", "r") as archivo:
		productos = archivo.readlines()
		for linea in productos:
			producto = linea.strip().split(",")
			lista.append({"nombre": producto[0], "precio": producto[1],  "cantidad": producto[2]})
	return lista


productos = generar_diccionario_productos()


def buscar_producto():
	nombre_producto = input("Ingrese el nombre del producto: ")

	with open("productos.txt", "r") as archivo:
		productos = archivo.readlines()
		existe = False
		for linea in productos:
			producto = linea.strip().split(",")
			if producto[0] == nombre_producto:
				print(f"Producto: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}")
				existe = True
		
		if not existe:
			print("ERROR:  No existe ese producto")

buscar_producto()

print("Guardando datos...")
with open("productos.txt", "w") as archivo:
	for producto in productos:
		archivo.write(f"{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n")


print("Datos guardados")

