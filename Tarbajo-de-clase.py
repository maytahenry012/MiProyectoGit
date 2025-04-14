# Solicitar al usuario la cantidad de estudiantes a regitar
cant = int(input("Ingresa la cantidad de estudiantes a registar: "))
mayores = 0
menores = 0
cantidad = 0
for i in range(0,cant):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    if edad >= 18:
        print(nombre, "Es mayor de edad")
        mayores = mayores + 1
    else: 
        print(nombre, "Es menor de edad")
        menores = menores + 1

    edad_futura = edad + 5
    print("En 5 años ", nombre, " tendra ", edad_futura, "años.")
    cantidad = cantidad + 1
    print(" ")
print(" ")
print("Cantidad de estudiantes registrados: ", cantidad)
print("Cantidad de estudiantes mayores: ", mayores)
print("Cantidad de estudiantes menores: ", menores)
print("")
numero = int(input("Introduce un numero para ver su tabla de multiplicar: "))
for i in range(1,11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

