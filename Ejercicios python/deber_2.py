edad = input("Ingrese su edad: ")
if int(edad) >= 18:
    print("Tienes la edad suficiente para conducir.")
else:
    edad_faltante = 18 - int(edad)
    print(f"Te faltan {edad_faltante} años para conducir.")
 
my_age = 16
your_age = input("Ingrese su edad: ")
if int(your_age) > my_age:
    diferencia = int(your_age) - my_age
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif int(your_age) < my_age:
    diferencia = my_age - int(your_age)
    if diferencia == 1:
        print("Eres 1 año menor que yo.")
    else:
        print(f"Eres {diferencia} años menor que yo.")
else:
    print("Tenemos la misma edad.")
 
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")   
 
puntaje = int(input("Ingrese su puntaje: "))
if 90 <= puntaje <= 100:
    print("Calificación: A")
elif 80 <= puntaje <= 89:
    print("Calificación: B")
elif 70 <= puntaje <= 79:
    print("Calificación: C")
elif 60 <= puntaje <= 69:
    print("Calificación: D")
elif 0 <= puntaje <= 59:
    print("Calificación: F")
 
Estación_del_año = input("Ingrese el mes: ")
if Estación_del_año in ["Septiembre", "Octubre", "Noviembre"]:
    print("La estación del año es Otoño.")
elif Estación_del_año in ["Diciembre", "Enero", "Febrero"]:
    print("La estación del año es Invierno.")
elif Estación_del_año in ["Marzo", "Abril", "Mayo"]:
    print("La estación del año es Primavera.")
elif Estación_del_año in ["Junio", "Julio", "Agosto"]:
    print("La estación del año es Verano.")
 
frutas = ['banana', 'orange', 'mango', 'lemon']
fruta_ingresada = input("Ingrese una fruta: ")
if fruta_ingresada in frutas:
    print("Esa fruta ya existe en la lista")
else:    frutas.append(fruta_ingresada)
print(frutas)
 