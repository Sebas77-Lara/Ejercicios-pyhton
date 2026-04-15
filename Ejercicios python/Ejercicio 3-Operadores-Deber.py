#1
edad = 16
#2
estatura = 1.75
#3
base = (float(input("Ingresa la base de tu triangulo: ")))
altura = (float(input("Ingresa la altura de tu triangulo: ")))
area = (base * altura) / 2
print("El área de tu triangulo es: ", area)
#4
lado1 = (float(input("Ingresa el primer lado de tu triangulo: ")))
lado2 = (float(input("Ingresa el segundo lado de tu triangulo: ")))
lado3 = (float(input("Ingresa el tercer lado de tu triangulo: ")))
perimetro = lado1 + lado2 + lado3
print("El perímetro de tu triangulo es: ", perimetro)
#5
longitud = (float(input("Ingresa la longitud de tu rectangulo: ")))
ancho = (float(input("Ingresa el ancho de tu rectangulo: ")))
area_rectangulo = longitud * ancho
perimetro_rectangulo = 2 * (longitud + ancho)
print("El área de tu rectangulo es: ", area_rectangulo)
print("El perímetro de tu rectangulo es: ", perimetro_rectangulo)
#6
radio = (float(input("Ingresa el radio de tu circulo: ")))
area_circulo = 3.14 * radio ** 2
circunferencia = 2 * 3.1416 * radio
print("El área de tu circulo es: ", area_circulo)
print("La circunferencia de tu circulo es: ", circunferencia)

#7
x1, x2 = 2, 6
y1, y2 = 2, 10
pendiente = (y2 - y1) / (x2 - x1)
disancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("La pendiente de la recta es: ", pendiente)
print("La distancia entre los puntos es: ", disancia)
#8
for x in range(-10, 1):
    y=x**2 + 6*x + 9
    print("El valor de y para x =", x, "es:", y)
# 9 
print(len("Python") > len("dragón"))
#10
print("on" in "Python" and "on" in "dragon")
#11
oracion = "Espero este curso no esté lleno de jerga"
print("jerga" in oracion)
#12
largo = (int(len("Python")))
valor_float = float(largo)
valot_string = str(largo)
print("El valor entero es: ", largo)
print("El valor flotante es: ", valor_float)
print("El valor string es: ", valot_string)
#13
print(7 // 3 == int(2.7))
#14
print(type(10) == type(10.0))
#15
print(int(9.8) == 10)
#16
horas = float(input("Ingresa el número de horas que trabajaste: "))
tarifa = float(input("Ingresa tu tarifa por hora: "))
salario = horas * tarifa
print("Tu salario es: ", salario)
#17
anios = int(input("Ingresa tu edad en años: "))
segundos = anios * 365 * 24 * 60 * 60
print("Tu edad en segundos es: ", segundos)
#18
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)











