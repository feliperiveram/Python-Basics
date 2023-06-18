import numpy as np

print("¡Bienvenid@ al programa!")
menu = 0
arreglo = 0
while menu != 4:
    print("¿Qué deseas realizar?:\n1.- GENERAR UN NUEVO ARREGLO\n2.- MOSTRAR LA SUMA DE LAS FILAS DEL ARREGLO\n3.- MOSTRAR EL PROMEDIO POR COLUMNAS DEL ARREGLO\n4.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu > 4 or menu < 1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        eje_x = input("Ingrese un valor entre 3 y 6 que desea que sea el tamaño horizontal de la matriz: ")
        while type(eje_x) == str:
            try:
                eje_x = int(eje_x)
                if eje_x > 6 or eje_x < 3:
                    eje_x = input("Valor ingresado debe estar entre 3 y 6. Ingrese nuevamente su opción: ")
            except ValueError:
                eje_x = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        eje_y = input("Ingrese un valor entre 3 y 6 que desea que sea el tamaño vertical de la matriz: ")
        while type(eje_y) == str:
            try:
                eje_y = int(eje_y)
                if eje_y > 6 or eje_y < 3:
                    eje_y = input("Valor ingresado debe estar entre 3 y 6. Ingrese nuevamente su opción: ")
            except ValueError:
                eje_y = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        arreglo = np.random.uniform(1,10,(eje_y,eje_x))
        print (f"Su arreglo es el siguiente:\n\n{arreglo}\n")
    # FILA HORIZONTAL
    elif menu == 2:
        if arreglo == 0:
            print("Debe crear un arreglo (opción 1 del menú principal) primero.")
        else:
            for n in range (eje_y):
                print (f"La suma de la fila {n+1} es {(arreglo[n,::]).sum()}")
    # PROMEDIO POR COLUMNAS (VERTICAL)
    elif menu == 3:
        if arreglo == 0:
            print("Debe crear un arreglo (opción 1 del menú principal) primero.")
        else:
            for m in range (eje_x):
                print(f"El promedio de la columna {m+1} es {(arreglo[::,m]).mean()}")
    else:
        print ("¡Gracias por haber usado el programa!")