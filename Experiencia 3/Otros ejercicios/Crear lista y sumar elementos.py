menu = 0
lista = []
while menu != 4:
    print("1.- INGRESAR NÚMERO A SUMAR\n2.- SUMAR LOS NÚMEROS INGRESADOS\n3.- BORRAR LISTA Y EMPEZAR DE NUEVO\n4.- SALIR DEL PROGRAMA")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>4 or menu<1:
                menu = input("El valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("El valor ingresado no es válido. Ingrese nuevamente su opción: ")
        if menu == 1:
            num = input("Ingrese el número a sumar: ")
            while type(num) == str:
                try:
                    num = float(num)
                except ValueError:
                    num = input("El valor ingresado no es válido. Ingrese nuevamente el número a sumar: ")
            lista.append(num)
        elif menu == 2:
            if len(lista)>1:
                paso = 0
                suma = 0
                while (paso <= (len(lista)-1)):
                    suma += lista[paso]
                    paso += 1
                print(f"La lista que usted ha creado es la siguiente:\n{lista}")
                print(f"La suma de los elementos es {suma}")
            elif len(lista) == 1:
                suma = lista[0]
                print(f"La lista que usted ha creado es la siguiente:\n{lista}")
                print(f"La suma de los elementos es {suma}")
            else:
                print("No ha agregado ningún elemento a la lista")
            lista = []
        elif menu == 3:
            lista = []
        else:
            print("Usted ha salido del programa. ¡Gracias por haberlo usado!")