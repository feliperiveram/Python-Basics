menu = 1
while menu != 2:
    # Ingresar un número y validarlo
    num = input("Ingrese el número del cual desea conocer su factorial: ")
    while type(num) == str:
        try:
            num = int(num)
            if num<=0:
                num = input("El número debe ser mayor o igual que 0, ingrese nuevamente su número: ")
        except ValueError:
            num = input("Valor no válido, ingrese nuevamente su opción: ")
    # Cálculo del factorial
    factorial = 1
    for elemento in range(1,num+1,1):
        factorial = elemento*factorial
    print(f"El factorial de {num} es {factorial}.")
    # Menú y validador
    print("1.- INGRESAR OTRO NÚMERO \n2.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("Valor no válido, ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor no válido, ingrese nuevamente su opción: ")