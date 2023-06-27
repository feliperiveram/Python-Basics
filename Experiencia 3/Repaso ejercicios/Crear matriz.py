import numpy as np

# • El arreglo poblado.• La suma por filas.• El promedio por columnas.
menu = 0
matriz = 0
print("¡Bienvenid@!")
while menu != 4:
    print("¿Qué deseas realizar hoy?:\n1.- CREAR UNA NUEVA MATRIZ\n2.- SUMAR CADA FILA\n3.- PROMEDIAR CADA COLUMNA\n4.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu > 4 or menu < 1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        eje_x = input("Ingrese el tamaño horizontal que desea que tenga la matriz (3 a 6): ")
        while type(eje_x) == str:
            try:
                eje_x = int(eje_x)
                if eje_x > 7 or eje_x < 3:
                    eje_x = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
            except ValueError:
                eje_x = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        eje_y = input("Ingrese el tamaño vertical que desea que tenga la matriz (3 a 6): ")
        while type(eje_y) == str:
            try:
                eje_y = int(eje_y)
                if eje_y > 7 or eje_y < 3:
                    eje_y = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
            except ValueError:
                eje_y = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        matriz = np.random.uniform(1,100,size=(eje_y,eje_x))
        print(f"La matriz generada es la siguiente:\n\n{matriz}\n")
    elif menu == 2:
        try:
            for y in range(eje_y):
                print(f"Suma de la fila {y+1}: {(matriz[y,:]).sum()}")
        except:
            print("Aún no se ha generado ninguna matriz.")
    elif menu == 3:
        try:
            for x in range(eje_x):
                print(f"Suma de la columna {x+1}: {(matriz[:,x]).mean()}")
        except:
            print("Aún no se ha generado ninguna matriz.")
    else:
        print("¡Gracias por haber usado el programa!")