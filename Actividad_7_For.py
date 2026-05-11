'''
numbers = [1, 2, 3, 4, 5]
suma = 0
for number in numbers:
    suma = suma + number
promedio = suma / len(numbers)

languaje = "Sebas Lara"
for letter in languaje:
    print("a")
'''

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