print("El siguiente programa tiene las siguientes funcionalidades: identificar paridad de un número y mostrar serie fibonacci de los primeros 10 números")
menu = 1
while menu != 2:
    # Menú de entrada
    print("1.- CONOCER PARIDAD DE UN NÚMERO \n2.- MOSTRAR SERIE FIBONACCI CON LÍMITE ESPECIFICADO")
    opcion = input("Ingrese la opción deseada: ")
    while type(opcion) == str:
        try:
            opcion = int(opcion)
            if  opcion>2 or opcion<1:
                opcion = input("Opción ingresada no es válida, ingrese nuevamente su opción: ") 
        except ValueError:
                opcion = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
    # Paridad
    if opcion == 1:
        num = input("Ingrese el número: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                    num = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
        if (num%2)==0:
             print(f"El número {num} es par.")
        else:
             print(f"El número {num} es impar.")
    # Fibonacci
    else:
        lista = []
        i = 1
        recorrer = 1
        fibonacci = [0,1]
        limite = input("Ingrese el número de elementos de la serie fibonacci (debe ser mayor a 0): ")
        while type(limite) == str:
            try:
                limite = int(limite)
                if limite<=0:
                    limite = input("Opción no es válida, ingrese nuevamente el número de elementos de la serie fibonacci: ")
            except ValueError:
                    limite = input("Opción no es válida, ingrese nuevamente el número de elementos de la serie fibonacci: ")
        if limite==1:
            print(f"La secuencia fibonacci de {limite} elementos es: ")
            print(fibonacci[0])
        elif limite==2:
            print(f"La secuencia fibonacci de {limite} elementos es: ")
            for elemento in fibonacci:
                print(elemento) 
        else:
            while i<=(limite-2):
                agregar = fibonacci[recorrer]+fibonacci[recorrer-1]
                fibonacci.append(agregar)
                i += 1
                recorrer += 1
            print(f"La secuencia fibonacci de {limite} elementos es: ")
            for elemento in fibonacci:
                print(elemento)
    # Menú de salida
    print("1.- VOLVER AL MENÚ PRINCIPAL \n2.- SALIR")
    menu = input("Ingrese la opción deseada: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("Opción ingresada no es válida, ingrese nuevamente su opción: ") 
        except ValueError:
                menu = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")