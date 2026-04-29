nombre= input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))
puntaje= int(input("Ingrese su puntaje: "))
asistencia= float(input("Ingrese su asistencia: ")) 
codigo= input("Ingrese su codigo: ")
print(nombre.capitalize())
promedio= (puntaje + asistencia) / 2
print("El promedio es: ", promedio)
if edad >= 14:
    if puntaje >= 80:
        if codigo == ("PYTHON2026"):
            print("Acceso VIP")
        else:
            print("Acceso regular")
    elif puntaje >= 60 and puntaje <=79:
        print("Acceso con observación")
    else:
        print("Acceso denegado por bajo rendimiento")
else:
    if codigo == ("PYTHON2026"):
        print("Acceso con especial con acompañante")
    else:
        print("No cumple la edad minima")
if puntaje >= 90 and asistencia >= 90:
    print("Candidato destacado")
elif puntaje >= 50 and asistencia >= 50:
    print("Requiere refuerzo previo")

    


