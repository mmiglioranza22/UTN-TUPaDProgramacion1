# # 1
# notas = [9, 6, 6, 7, 5, 3, 10, 9, 8, 7]

# print(notas)

# promedio = 0
# alta = 0
# baja = 10

# for nota in notas:
# 	promedio += nota
# 	if (nota > alta):
# 		alta = nota
# 	if (nota < baja):
# 		baja = nota

# print(f"Promedio: {promedio / 10}, Más alta: {alta}, más baja: {baja}")


# # 2

# productos = []
# while len(productos) < 5:
# 	producto = input("Ingrese un producto: ")
# 	productos.append(producto)

# lista_ordenada = sorted(productos)

# print(lista_ordenada)

# eliminado = input('Elimine un elemento: ')

# lista_ordenada.remove(eliminado)

# print(lista_ordenada)


# # 3

# import random

# lista_pares = []
# lista_impares = []

# for i in range(15):
# 	numero = random.randint(1, 100)

# 	if numero % 2 == 0:
# 		lista_pares.append(numero)
# 	else:
# 		lista_impares.append(numero)


# # 4

# datos = [1, 3, 5, 3, 7, 1 ,9, 5, 3]

# datos_limpios = list(set((datos)))

# print(datos_limpios)


# # 5

# estudiantes = ["Juan", "Pedro", "Maria", "Manuel", "Paco", "Jean-Yves", "Giacomo", "Máximo"]

# print(estudiantes)

# accion = input("Elija una acción (E: eliminar, A: agregar)")

# if accion == "E":
# 	estudiante = input("Elija el estudiante a eliminar: ")
# 	estudiantes.remove(estudiante)
# 	print(estudiantes)
# elif accion == "A":
# 	estudiante = input("Ingrese el nuevo estudiante: ")
# 	estudiantes.append(estudiante)
# 	print(estudiantes)
# else: 
# 	print("Opción inválida.")


# # 6

# lista = list(range(1, 8, 1))
# ultimo = lista[-1]
# nueva_lista = [ultimo] + lista[:-1]

# print(nueva_lista)

# # 7

# from statistics import mean

# temp_minimas = [8.4, 9.2, 2.3, 2.0, 7.1, 6.1, 7.0]
# temp_maximas = [22.2, 22.3, 24.1, 25.3, 19.1, 21.1, 20.1]

# temperaturas = [temp_minimas, temp_maximas]
# promedio_minimas = mean(temperaturas[0],)
# promedio_maximas = mean(temperaturas[1])

# print(f"Promedio temp mínimas: {promedio_minimas:.2f}")
# print(f"Promedio temp máximas: {promedio_maximas:.2f}")

# temp_max = 0

# for t in temperaturas[1]:
# 	if t > temp_max:
# 		temp_max = t

# dia = temperaturas[1].index(temp_max)

# if dia == 0:
# 	print(f"El lunes se registró la temperatura más alta: {temp_max}")
# elif dia == 1:
# 	print(f"El martes se registró la temperatura más alta: {temp_max}")
# elif dia == 2:
# 	print(f"El miércoles se registró la temperatura más alta: {temp_max}")
# elif dia == 3:
# 	print(f"El jueves se registró la temperatura más alta: {temp_max}")
# elif dia == 4:
# 	print(f"El viernes se registró la temperatura más alta: {temp_max}")
# elif dia == 5:
# 	print(f"El sábado se registró la temperatura más alta: {temp_max}")
# else:
# 	print(f"El domingo se registró la temperatura más alta: {temp_max}")


# # 8

# matriz_notas = [
# 	[6, 7, 2],
# 	[10, 9, 10],
# 	[7, 8, 7],
# 	[9, 9, 5],
# 	[4, 9, 8]
# ]

# for index, estudiante in enumerate(matriz_notas):
# 	suma_notas_alumno = 0
# 	for nota in estudiante:
# 		suma_notas_alumno += nota
# 	print(f"Promedio alumno N {index + 1}: {suma_notas_alumno / 3:.2f}")


# 9

tablero = [
	["-", "-", "-"],
	["-", "-", "-"],
	["-", "-", "-"]
]

while True:
	fila_jugador_1 = int(input("Jugador 1: Ingrese fila: 0 - 3: "))
	columna_jugador_1 = int(input("Jugador 1: Ingrese columna: 0 - 3: "))
	tablero[fila_jugador_1][columna_jugador_1] = "X"

	for fila in tablero:
		print(fila, sep="\n")
		
	fila_jugador_2 = int(input("Jugador 2: Ingrese fila: 0 - 3: "))
	columna_jugador_2 = int(input("Jugador 2: Ingrese columna: 0 - 3: "))
	tablero[fila_jugador_2][columna_jugador_2] = "O"

	for fila in tablero:
		print(fila, sep="\n")