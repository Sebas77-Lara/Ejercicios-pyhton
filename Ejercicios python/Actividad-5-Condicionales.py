numero = int(input("Numero: "))
if numero != 0:
    if numero > 0:
        print("El numero es positivo")
        if numero % 2 == 0:
            print("El numero es par")
        else: 
            print("El numero es impar")
    else:
        print("El numero es negativo")
        if numero % 2 != 0:
            print("El numero es impar")
        else :
            print("El numero es par")
else:
    print("El numero es cero")

edad = int(input("Edad: "))
print("Eres mayor de edad" if edad >= 18 else "Eres menor de edad")


