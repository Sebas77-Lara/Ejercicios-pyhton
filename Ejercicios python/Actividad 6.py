count = 0 
while count < 5:
    count = count + 1
    if count == 3:
        continue
    print(count)
    
intentos = 0

x= input("Ingrese la contraseña: ")
while intentos <2:
    x = input("Ingrese la contraseña: ")
    intentos = intentos + 1
    if x == "python123":
        print("Contraseña correcta")
        break
else:
    print('bruhhh muchos intentos')
