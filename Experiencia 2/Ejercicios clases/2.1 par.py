menu=0
while menu != 2:
    num = int(input("Ingrese un número entero entre 1 y 101: "))
    while num<=1 or num>=101:
        num = int(input("El número debe estar entre 1 y 101. Ingrese nuevamente un número: "))
    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")
    print(" 1.- INGRESAR OTRO NÚMERO. \n 2.- SALIR DEL PROGRAMA.")
    int(input("Ingrese su opción: "))