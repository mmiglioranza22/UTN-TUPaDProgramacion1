# Kata: Estructuras condicionales

## Ejercicio 1

# 1 Leer el codigo y explicar qué hace:

# Paso a explicar el código linea por línea
# la variable contrasena_correcta asigna la cadena "programacion1" y la guarda en memoria
contrasena_correcta = "programacion1"
# la variable contrasena_usuario imprime por pantalla de la consula "Introduce la contraseña: " y toma la entrada por consola que se ingrese
contrasena_usuario = input("Introduce la contraseña: ")

# El condicional if compara con un operador relacional de igualdad (==) si la contraseña ingresada por el usuario por consola es la misma que la correcta
if contrasena_usuario == contrasena_correcta:
#  Si son iguales, imprime por pantalla que es correcta
 print("Contraseña correcta. Bienvenido.")
#  Caso contrario, imprime por pantalla que la contraseña es incorrecta y luego el programa termina
else:
 print("Contraseña incorrecta. Intenta de nuevo.") 


# Si el usuario ingresa la contraseña con mayúsculas el programa va a imprimir que es incorrecta. Tiene que ser idéntica para ser correcta

# Para dar más intentos se podría incluir la lógica del input en un ciclo while para que salga (break) sólo si la contraseña es correcta.


## Ejercicio 2

vocal = input("Ingrese una vocal: ").lower() 

if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
 print("La letra ingresada es una vocal")
else:
 print("La letra ingresada no es una vocal") 

#  Para manejar las vocales acentuadas, es necesario incluirlas en la condicion if
#  Para simplificar las comparaciones, se podría guardar en un variable (eg: es_vocal = vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u")
#  y verificar en el if esa variable para una mejor lectura. 
#  También se podría usar un match-case (similar al switch de otros lenguajes) para hacer la comparación más sencilla.


## Ejercicio 3

numero = int(input("Ingrese un número: "))

if numero > 0:
 print("El número es positivo")
elif numero < 0:
 print("El número es negativo")
else:
 print("El número es cero")


# Si el usuario ingresa un texto, el programa revienta y arroja un ValueError porque la variable numero castea la entrada por consola a un número entero.
# Para número decimales, usaría float() para el input() y aclararía que se pueden ingresar decimales


## Ejercicio 4

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))

if primer_numero > segundo_numero:
 print("El primer número ingresado es mayor")
elif primer_numero < segundo_numero:
 print("El primer número ingresado es menor")
else:
 print("Los números ingresados son iguales")

# Si se quiere comparar más números, es decir, que el programa no termine pero comparando siempre de a 2 números, se puede incluir un bucle que siga pidiendo números para comprar una vez hecha la primer comparación
# Si se ingresan otros valores que no sean número, el programa revienta y arroja ValueError (porque se está casteando el input a números enteros con la función int())



## Ejercicio 5 

temperatura = int(input("Ingrese la temperatura en celcius: "))

frio = temperatura <= 10
templado = temperatura > 10 and temperatura <= 25
calor = temperatura > 25

if frio:
 print("Hace frío")
elif templado:
 print("Está templado")
else:
 print("Hace calor")

 # Para usar celcius habría que modificar el input para tomar valores float y indicar que tome la temperatura en fahrenheit
 # y es necesario convertir los enteros que se usan para comparar cada temperatura (10 y 25) y convertirlos a fahrenheit

# Para añadir más rangos primero hay que definir qué variable lo representa (mucho frio -> temperatura <=0, por ejemplo, y modificar el rango para frio -> entre 0 y 10)
# y luego incluirlo en el programa como un caso de comparación más (podría ser en el if inicial, por ejemplo)

## Ejercicio 6

anio = int(input("Ingrese un año: "))

es_bisiesto = (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0)

if es_bisiesto:
 print("Se ingresó un año bisiesto")
else:
 print("Se ingresó un año no bisiesto") 

 # 1900 no es bisiesto porque el resto de su division por 400 no es 0, tampoco el resto de su division por 4 es 0 y el resto de su division por 100 sí es 0
 # para validar que el año sea positivo se agrega un if al principio que chequea si el número es mayor a 0



## Ejercicio 7

frase = input("Ingrese una frase: ")

ultimo_caracter = len(frase) -1

if frase[ultimo_caracter] == ".":
 print(frase)
else:
 print(frase + ".")

# Si se considera que los espacios al final de la frase no cuentan para la frase (porque el espacio es un caracter), se usa el método strip() de las cadenas para eliminarlos (idealmente al momento de asignar la entrada a la variable frase)
# No entiendo la pregunta: se puede considerar cualquier otro caracter, pero depende que lógica se quiere hacer (si una frase termina con coma, punto y coma, etc, y se la quiere reemplazar por punto, es necesaario adaptar la lógica para que en vez de concatenar un punto al final de la frase, reemplazarlo)


## Ejercicio 8

contraseña = input("Ingrese su contraseña: ").strip()

mas_de_ocho_caracteres = len(contraseña) > 8
menos_de_20_caracteres = len(contraseña) <= 20
tiene_mayuscula = False
tiene_digito = False

for caracter in contraseña:
 if caracter.isupper():
  tiene_mayuscula = True
  break

for caracter in contraseña:
 if caracter.isdigit():
  tiene_digito = True
  break
  
if mas_de_ocho_caracteres and menos_de_20_caracteres and tiene_mayuscula and tiene_digito:
 print("¡Felicitaciones! Creaste tu contraseña.")
else:
 print("La contraseña no es segura.")

# Para añadir un caracter especial, crearía una variable tiene_caracter_especial inicializada en False y chequearía con un bucle for in que al menos un caracter no sea alfanumérico.
# se usa isalnum() para ver si es alfanumérico y se niega esa condicion. Caso de que al menos 1 caracter no sea alfanumérico, se asigna True a la variable tiene_caracter_especial
# Es una buena práctica limitar la longitud máxima primero para no tener contraseñas demasiado largas y difíciles de recordar por el usuario y de comparar por el programa


