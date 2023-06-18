import math

# Definición de funciones
def area_circulo(a): #(Pi)*(r**2)
    return ((math.pi)*(a**2))

def perim_cuadrado(l):
    return (l*4)

# Programa
print("¡Bienvenid@ al programa!")
menu = 0
while menu != 4:
    print("¿Qué deseas realizar?:\n1.- CONOCER EL ÁREA DE UN CÍRCULO\n2.- CONOCER EL PERÍMETRO DE UN CUADRADO\n3.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu > 3 or menu < 1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        radio = input("Ingrese el radio del círculo: ")
        while type(radio) == str:
            try:
                radio = float(radio)
                if (radio <= 0):
                    radio = input("Valor ingresado debe ser mayor a 0. Ingrese nuevamente el valor del radio: ")
            except ValueError:
                radio = input("Valor ingresado no es válido. Ingrese nuevamente el valor del radio: ")
        print(f"El valor del área de un círculo de radio {radio} es {area_circulo(radio)}.")
    elif menu == 2:
        lado = input("Ingrese el lado del cuadrado: ")
        while type(lado) == str:
            try:
                lado = float(lado)
                if (lado <= 0):
                    lado = input("Valor ingresado debe ser mayor a 0. Ingrese nuevamente el valor del lado: ")
            except ValueError:
                lado = input("Valor ingresado no es válido. Ingrese nuevamente el valor del lado: ")
        print(f"El valor del perímetro de un cuadrado de lado {lado} es {perim_cuadrado(lado)}.")
    else:
        print("¡Gracias por haber usado el programa!")