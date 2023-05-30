menu = 0
while menu != 3:
    print("¡Bienvenid@! ¿Qué quieres realizar hoy?\n1.- DIVISIÓN DE DOS NÚMEROS\n2.- PARIDAD DE UN NÚMERO\n3.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>3 or menu<1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        dividendo = input("Ingrese el dividendo (a) de la siguiente expresión 'a/b': ")
        while type(dividendo) == str:
            try:
                dividendo = float(dividendo)
            except ValueError:
                dividendo = input("Valor ingresado no es válido. Ingrese nuevamente su dividendo: ")
        divisor = input(f"Ingrese el divisor (b) de la siguiente expresión '{dividendo}/b': ")
        while type(divisor) == str:
            try:
                divisor = float(divisor)
            except ValueError:
                divisor = input("Valor ingresado no es válido. Ingrese nuevamente su divisor: ")
        try:
            resultado = dividendo/divisor
            print(f"El resultado de {dividendo}/{divisor} es {resultado}.")
        except ZeroDivisionError:
            print(f"Una división se puede realizar siempre y cuando el divisor sea distinto de 0.")
    elif menu == 2:
        num = input("Ingrese el número del cual desea conocer su paridad: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese nuevamente su número: ")
        division = num%2
        if division == 0:
            print(f"El número {num} es par.")
        else:
            print(f"El número {num} es impar.")
    else:
        print("¡Gracias por usar el programa, que tengas un buen día!")