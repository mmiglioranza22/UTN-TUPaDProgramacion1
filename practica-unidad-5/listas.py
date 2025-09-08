# 1
notas = [9, 6, 6, 7, 5, 3, 10, 9, 8, 7]

print(notas)

promedio = 0
alta = 0
baja = 10

for nota in notas:
	promedio += nota
	if (nota > alta):
		alta = nota
	if (nota < baja):
		baja = nota

print(f"Promedio: {promedio / 10}, Más alta: {alta}, más baja: {baja}")


# 2

productos = []
while len(productos) < 5:
	producto = input("Ingrese un producto: ")
	productos.append(producto)

lista_ordenada = sorted(productos)

print(lista_ordenada)

eliminado = input('Elimine un elemento: ')

lista_ordenada.remove(eliminado)

print(lista_ordenada)


# 3

import random

lista_pares = []
lista_impares = []

for i in range(15):
	numero = random.randint(1, 100)

	if numero % 2 == 0:
		lista_pares.append(numero)
	else:
		lista_impares.append(numero)


# 4

datos = [1, 3, 5, 3, 7, 1 ,9, 5, 3]

datos_limpios = list(set((datos)))

print(datos_limpios)


# 5

estudiantes = ["Juan", "Pedro", "Maria", "Manuel", "Paco", "Jean-Yves", "Giacomo", "Máximo"]

print(estudiantes)

accion = input("Elija una acción (E: eliminar, A: agregar)")

if accion == "E":
	estudiante = input("Elija el estudiante a eliminar: ")
	estudiantes.remove(estudiante)
	print(estudiantes)
elif accion == "A":
	estudiante = input("Ingrese el nuevo estudiante: ")
	estudiantes.append(estudiante)
	print(estudiantes)
else: 
	print("Opción inválida.")








