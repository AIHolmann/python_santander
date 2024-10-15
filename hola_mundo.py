print ("¡Hola, Mundo!")
#coment
#en python es True y False, la primer letra con mayúscula
print(3 ** 10)
print(10 // 3)
print(10 / 3)

#listas de compresion
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)

#funciones
def saludo(nombre):
    print(f"¡Hola, {nombre} desde la funcionn!")
saludo("Alejo")

#retorno
def suma(a,b):
    return a+b

resultado = suma(5,15)
print(resultado)

#anónimas
cuadrado = lambda x: x ** 2
print(cuadrado(7))

#el scoope de las variables puede ser local(las definidas dentro de una funcion) o global(fuera de cualquier funcion)

#multiples argumentos:
def calcular_media(*numeross):
    """
    Calcula la media, recibiendo la cantidad de parametros que se desee
    """
    sumanueva = sum(numeross)
    cantidad = len(numeross)
    media = sumanueva/cantidad
    return media

print("Media: ", calcular_media(10,25,40))

#docstrings: documentacion de la funcion ->
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

#ENTRADAS / SALIDAS
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")
if int(edad) >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#LECTURAS Y ESCRITURAS de archivos
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#IMPORTACION Y CREACION de modulos