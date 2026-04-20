# ===== PARTE A =====
# Respuesta 1:
nombre = "Lucía"
edad = 16
promedio = 9.75
cursos = ["Python", "HTML", "CSS"]
print(type(nombre))
print(type(edad))
print(type(promedio))
print(type(cursos))
print(len(nombre))
#Responde:
# A: Indica el tipo de dato de cada variable : 
""" nombre = 'str'
edad = 'int'
promedio = 'float'
cursos = 'list' """

# B: Escribe qué mostraría el programa en pantalla.
""" <class 'str'>
<class 'int'>
<class 'float'>
<class 'list'>
5 """ 

# C: Explica qué hace len(nombre) : 
""" La función len() devuelve la cantidad de caracteres que tiene la variable nombre, 
en este caso, el resultado es 5 porque "Lucía" tiene 5 caracteres."""

# Respuesta 2:
# a) ¿Qué diferencia hay entre print() e input()?
#La función print se utiliza para mostrar información en la pantalla
# mientras que input se ayuda a solicitar al usuario que ingrese información desde el teclado. 

#b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
# Porque la función input() devuelve un valor de tipo cadena (string), 
# y si se intenta usar ese valor directamente en un cálculo matemático, saldra error

# c) Explica la diferencia entre /, // y %.
# El operador / realiza una división normal y devuelve un resultado de tipo float, 
#mientras que // realiza una división entera y % modulo es el que devuelve el residuo de la división.

# d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.
#python --version
# e) Escribe una instrucción que permita consultar las palabras reservadas de Python.
#import keyword

# ===== PARTE B =====
# El siguiente programa tiene errores. Reescríbelo de forma correcta para que funcione.
ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print("Área total: " + str(area))
print("Costo estimado: " + str(costo))

#Luego responde:
#a) ¿Cuáles eran los errores principales?
#Los errores principales eran que las variables ancho, largo y precio no estaban definidas como números, lo que causaba un error al intentar realizar cálculos con ellas.
#b) ¿Por qué tu corrección sí permite obtener resultados válidos?
#Mi corrección permite obtener resultados válidos porque ahora las variables ancho, largo y precio se definen como números de punto flotante (float) utilizando la función float(), lo que permite realizar cálculos matemáticos correctamente.

#Escribe un fragmento de código que haga lo siguiente:
#1. Cree la variable frase con el texto "Tecnología para todos".
#2. Muestre la frase en mayúsculas.
#3. Muestre la cantidad de caracteres de la frase.
#4. Verifique si la palabra "Python" está dentro de la frase.
#5. Reemplace "Tecnología" por "Programación".
#6. Divida la frase en palabras usando split().

frase = "Tecnología para todos"
print(frase.upper())
print(len(frase))
print("Python" in frase)
frase_reemplazada = frase.replace("Tecnología", "Programación")
print(frase_reemplazada)
palabras = frase.split()
print(palabras)

# ===== PARTE C =====
# 1. Solicite al usuario: Nombre, apellido, país, ancho de la pared, alto de la pared, precio por metro cuadrado
# Calcule: área de la pared, costo total estimado
# 2. Cree la variable nombre_completo.
# 1. Muestre un reporte final que incluya:
# nombre completo, país, área calculada, costo total (La impresión del reporte final debe
# realizarse usando f-strings.)
# 3. Muestre además:
# nombre_completo en mayúsculas
# la longitud de nombre_completo
# si la letra "a" está presente en nombre_completo
# si el costo total es mayor que 100 

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
ancho_pared = float(input("Ingrese el ancho de la pared en metros: "))
alto_pared = float(input("Ingrese el alto de la pared en metros: "))
precio_metro_cuadrado = float(input("Ingrese el precio por metro cuadrado: "))
area_pared = ancho_pared * alto_pared
costo_total = area_pared * precio_metro_cuadrado
nombre_completo = f"{nombre} {apellido}"
print (f"Reporte Final:\nNombre Completo: {nombre_completo}\nPaís: {pais}\nÁrea Calculada: {area_pared} metros cuadrados\nCosto Total: {costo_total}")
print(nombre_completo.upper())
print(len(nombre_completo))
print("a" in nombre_completo)
if costo_total > 100:
    print("El costo total es si es mayor que 100.")
else:    print("El costo total no es mayor que 100.")
