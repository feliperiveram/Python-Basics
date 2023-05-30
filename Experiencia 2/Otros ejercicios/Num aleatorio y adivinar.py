import random
menu = 1
while menu != 2:
    num_aleatorio = random.randint(1, 10)
    flag = False
    while flag == False:
        num = input("Ingrese el número entero entre 1 y 10 que ud. cree que es: ")
        while type(num) == str:
            try:
                num = int(num)
                if num <= 0 or num>10:
                    num = input("El número ingresado es incorrecto, este debe estar entre 1 y 10. Inténtelo nuevamente: ")
            except ValueError:
               num = input("El valor ingresado es incorrecto. Inténtelo nuevamente: ")
        if num == num_aleatorio:
            print(f"¡Es correcto, el número era el {num_aleatorio}!")
            flag = True
        else:
            if num>num_aleatorio:
                print(f"El {num} es mayor que la incógnita.")
            else:
                print(f"El {num} es menor que la incógnita.")
            flag == False
    print("1.- VOLVER A JUGAR\n2.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu<1 or menu>2:
                menu = input("La opción ingresada no es válida. Inténtelo nuevamente: ")
        except ValueError:
            menu = input("La opción ingresada no es válida. Inténtelo nuevamente: ")