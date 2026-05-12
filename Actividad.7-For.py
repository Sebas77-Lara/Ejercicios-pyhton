'''
numbers = [1, 2, 3, 4, 5]
suma = 0
for number in numbers:
    suma = suma + number
promedio = suma / len(numbers)

languaje = "Sebas Lara"
for letter in languaje:
    print("a")


a = input("Ingrese palabra: ")
vocales= 0 
consonantes= 0 
for x in a:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        vocales = vocales + 1
    else:
        consonantes = consonantes + 1
print ("El numero de vocales es : ", vocales)
print ("Y el numero de consonantes es de: ", consonantes)

companies = {"Facebook", "Google", "Facebook", "Amazon"}
for me in companies:
    print (me)
    if companies == "Facebook":
    
    
number = [ 1, 2, 3, 4, 5]
x = int(input("Ingrese num: "))
for y in number:
    if y == x:
        print ("Ganaste")
        break
else:
    print("perdiste")



    Realizar los ejercicios en Visual Studio Code y realizar el comit a GitHub
actividad 7 ciclos
EJERCICIO LISTAS
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
Escribe un programa que recorra la lista con un ciclo for y determine:
1. La suma total de las notas.
2. El promedio del curso.
3. Cuántos estudiantes aprobaron.
4. Cuántos estudiantes reprobaron.
Considera que aprueba quien tiene nota mayor o igual a 7.
EJERCICIOS STRING
Dada la siguiente contraseña:
contrasena = "Python2026"
Escribe un programa que recorra la contraseña con un ciclo for y determine:
1. Cuántas letras tiene.
2. Cuántos números tiene.
3. Cuántas veces aparece la letra "o".
EJERCICIOS CON SET
Dado el siguiente conjunto:
productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
Escribe un programa que recorra el conjunto con for y determine:
1. Cuántos productos únicos hay.
2. Cuántos productos tienen más de 6 letras.
No uses funciones como len().
EJERICIOCS CON BREAK
Obtener el usuario de un correo
Escribe un programa que pida al usuario ingresar su correo electrónico.
El programa debe recorrer el correo con un ciclo for y construir el nombre de
usuario, es decir, la parte que está antes del símbolo @.
Cuando el ciclo encuentre @, debe detenerse usando break.
EJERICIO CON CONTINUE
Pide al usuario que ingrese un número de teléfono.
El teléfono puede tener espacios o guiones.
El programa debe construir una versión limpia del teléfono, sin espacios ni
guiones.
'''

# Deber 
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma = 0
aprobados = 0
reprobados = 0
for nota in notas:
    suma = suma + nota
    if nota >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
promedio = suma / len(notas)
print("La suma total de las notas es: ", suma)
print("El promedio del curso es: ", promedio)
print("El numero de estudiantes aprobados es: ", aprobados)
print("El numero de estudiantes reprobados es: ", reprobados)

contraseña = "Python2026"
letras = 0
numeros = 0
o_count = 0
for char in contraseña:
    if char.isalpha():
        letras = letras + 1
    elif char.isdigit():
        numeros = numeros + 1
    if char == "o" or char == "O":
        o_count = o_count + 1
print("La contraseña tiene ", letras, " letras.")
print("La contraseña tiene ", numeros, " números.")
print("La letra 'o' aparece ", o_count, " veces.")

productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
productos_unicos = set()
productos_mas_de_6_letras = 0
for producto in productos:
    productos_unicos.add(producto)
    if len(producto) > 6:
        productos_mas_de_6_letras = productos_mas_de_6_letras + 1
print("El numero de productos únicos es: ", len(productos_unicos))
print("El numero de productos con mas de 6 letras es: ", productos_mas_de_6_letras)

correo = input("Ingrese su correo electrónico: ")
usuario = ""
for char in correo:
    if char == "@":
        break
    usuario = usuario + char
print("El nombre de usuario es: ", usuario)
telefono = input("Ingrese su número de teléfono: ")
telefono_limpio = ""
for char in telefono:
    if char == " " or char == "-":
        continue
    telefono_limpio = telefono_limpio + char
print("El número de teléfono limpio es: ", telefono_limpio)




