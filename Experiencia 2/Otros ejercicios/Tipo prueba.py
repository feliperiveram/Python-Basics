'''programa para ver si los números ingresados son primos, positivos o pares y contar'''
menu = 0
primos = 0
positivos = 0
pares = 0
numeros = 0
ingresados = []
while menu != 2:
    print("¡Bienvenid@!, ¿qué deseas hacer?:\n1.- INGRESAR UN NÚMERO\n2.- MOSTRAR INFORMACIÓN DE LOS NÚMEROS INGRESADOS")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu==1:
        divisores = 0
        num = input("Ingrese el número: ")
        while type(num) == str:
            try:
                num = int(num)
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese nuevamente el número: ")
        ingresados.append(num)
        if num>0:
            positivos += 1
        if (num%2)==0:
            pares += 1
        if num!=1 and num<0:
            num = num*(-1)
            i = 1
            divisores = 0
            division = 0
            while i<=num:
                division = num%i
                if division==0:
                    divisores += 1
                i += 1
        elif num!=1 and num>0:
            i = 1
            divisores = 0
            division = 0
            while i<=num:
                division = num%i
                if division==0:
                    divisores += 1
                i += 1
        if divisores == 2:
            primos += 1
        numeros += 1
    #RESUMEN DE LO ANTERIOR
    else:
        print(f"Estos fueron sus números: {ingresados}.")
        print(f"De los {numeros} números, {positivos} son positivos, {primos} son primos y {pares} son pares. ¡Gracias por usar el programa!")