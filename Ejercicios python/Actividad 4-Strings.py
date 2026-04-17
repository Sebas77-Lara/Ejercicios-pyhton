X = ("Programación para todos")
print (X)
cantidad_caracteres = len (X)
print(cantidad_caracteres)

print(X.upper())
print(X.lower())
print(X.title())
print(X.capitalize())

print(X.startswith("Programación"))
print(X.endswith("todos"))
print(X.find("para"))
print("Python" in X)

nuevo_texto = X.replace("Programación", "Python")
print(nuevo_texto)

letra1 = X[0]
print (letra1)
ultima = X[-1]
print(ultima)
posicion = X[5]
print(posicion)

nombre = "Sebastián"
print(f"Hola, mi nombre es {nombre}.")

iniciales = "".join([palabra[0].upper() for palabra in nombre.split()])
print(iniciales)
