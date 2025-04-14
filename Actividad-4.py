# imprime un mensaje de bienvenida
print("!Hola, bienvenido a tu primer programa en Python")
#Pedimos datos al usuario
nombre = input("Como te llamas")
edad = int(input("Cuantos años tienes"))
#Mostramos los datos del usuario
print("Hola", nombre, "tienes", edad, "años")
#condicionales
if edad >= 18:
    print("Eres mayor de edad...")
else:
    print("Eres menor de edad...") 
#Bucles 
numero = int(input("Introduce un numero para ver su tabla de multiplicar: "))
for i in range(1,11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
# Bucles While 
num = -1
while num != 0:
    num = int(input("Escribe un numero (0 para salir): "))
    print("Ingresaste: ", num)
