import numpy as np

print("¡Bienvenid@ al programa!")
menu = 0
while menu != 3:
    print("¿Qué deseas realizar?:\n1.- GENERAR UN ARREGLO U OTRO NUEVO\n2.- ADIVINAR SI UN NÚMERO ESTÁ O NO EN EL ARREGLO\n3.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu > 3 or menu < 1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        arreglo = np.random.randint(1,11,10)
        print ("El arreglo generado tiene 10 números enteros aleatorios entre 1 y 10, pudiendo tomar estos 2 valores.")
    if menu == 2:
        num = input("Ingrese el número que cree que está en el arreglo: ")
        while type(num) == str:
            try:
                num = int(num)
                if num > 10 or num < 1:
                    num = input("El valor que quiere analizar debe estar entre 1 y 10. Ingrese nuevamente su opción: ")
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        if num in arreglo:
            print (f"¡Adivinaste! El {num} se encuentra dentro del arreglo.")
        else:
            print (f"El {num} no se encuentra en el arreglo.")
    else:
        print ("¡Gracias por haber usado el programa!")