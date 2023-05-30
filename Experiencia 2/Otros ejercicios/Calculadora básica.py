'''calculadora básica'''
menu = 0
while menu != 5 :
    print("Ingrese la operación que desea realizar:\n1.- SUMAR\n2.- RESTAR\n3.- DIVIDIR\n4.- MULTIPLICAR\n5.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>5 or menu<1:
                menu = input("Valor ingresado no es válido. Ingrese su opción nuevamente: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese su opción nuevamente: ")
    #SUMA
    if menu == 1:
        suma = 0
        num = input("Ingrese su número: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
        suma += num
        opcion = 0
        while opcion != 2:
            print("1.- INGRESAR OTRO NÚMERO\n2.- SUMAR LOS NÚMEROS INGRESADOS")
            opcion = input("Ingrese su opción: ")
            while type(opcion) == str:
                try:
                    opcion = int(opcion)
                    if opcion>2 or opcion<1:
                        opcion = input("Valor ingresado no es válido. Ingrese su opción nuevamente: ")
                except ValueError:
                    opcion = input("Valor ingresado no es válido. Ingrese su opción nuevamente: ")
            if opcion == 1:
                num = input("Ingrese su número: ")
                while type(num) == str:
                    try:
                        num = float(num)
                    except ValueError:
                        num = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
                suma += num
        print(f"La suma de los números ingresados es {suma}.")
    #RESTA
    elif menu == 2:
        num = input("Ingrese su número: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
        resta = num
        opcion = 0
        while opcion != 2:
            print("1.- INGRESAR OTRO NÚMERO A RESTAR\n2.- RESTAR LOS NÚMEROS INGRESADOS")
            opcion = input("Ingrese su opción: ")
            while type(opcion) == str:
                try:
                    opcion = int(opcion)
                    if opcion>2 or opcion<1:
                        opcion = input("Valor ingresado no es válido. Ingrese su opción nuevamente: ")
                except ValueError:
                    opcion = input("Valor ingresado no es válido. Ingrese su opción nuevamente: ")
            if opcion == 1:
                num = input("Ingrese su número: ")
                while type(num) == str:
                    try:
                        num = float(num)
                    except ValueError:
                        num = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
                resta = resta-num
        print(f"La resta de los números ingresados es {resta}.")
    #DIVISIÓN
    elif menu == 3:
        num1 = input("Ingrese el número 'a' de 'a/b': ")
        while type(num1) == str:
            try:
                num1 = float(num1)
            except ValueError:
                num1 = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
        num2 = input(f"Ingrese el número 'b' de '{num1}/b': ")
        while type(num2) == str:
            try:
                num2 = float(num2)
            except ValueError:
                num2 = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
        try:
            division = num1/num2
            print(f"{num1} dividido en {num2} es {division}.")
        except ZeroDivisionError:
            print("Una división solamente se puede realizar si el divisor es distinto de 0.")
    #MULTIPLICACIÓN
    elif menu == 4:
        multiplicacion = 0
        num = input("Ingrese su número: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
        multiplicacion = num
        num = input("Ingrese su número: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
        multiplicacion = multiplicacion*num
        opcion = 0
        while opcion != 2:
            print("1.- INGRESAR OTRO NÚMERO A MULTIPLICAR\n2.- MULTIPLICAR LOS NÚMEROS INGRESADOS")
            opcion = input("Ingrese su opción: ")
            while type(opcion) == str:
                try:
                    opcion = int(opcion)
                    if opcion>2 or opcion<1:
                        opcion = input("Valor ingresado no es válido. Ingrese su opción nuevamente: ")
                except ValueError:
                    opcion = input("Valor ingresado no es válido. Ingrese su opción nuevamente: ")
            if opcion == 1:
                num = input("Ingrese su número: ")
                while type(num) == str:
                    try:
                        num = float(num)
                    except ValueError:
                        num = input("Valor ingresado no es válido. Ingrese su número nuevamente: ")
                multiplicacion = multiplicacion*num
        print(f"La multiplicación de los números ingresados es {multiplicacion}.")       
    #SALIR
    else:
        print("¡Gracias por usar la calculadora!")