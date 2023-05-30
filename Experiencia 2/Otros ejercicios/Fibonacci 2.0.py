op = 0
while op != 3:
    print("1.- PARIDAD DE UN NÚMERO\n2.- SECUENCIA FIBONACCI HASTA N\n3.- SALIR")
    op = input("Ingrese su opción: ")
    while type(op) == str:
        try:
            op = int(op)
            if op>3 or op<1:
                op = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")             
        except ValueError:
            op = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if op == 1:
        num = input("Ingrese un número: ")
        while type(num) == str:
            try:
                num = int(num)          
            except ValueError:
                op = input("Valor ingresado no es válido. Ingrese nuevamente su número: ")
        par = num%2
        if par == 0:
            print(f"El número {num} es par.")
        else:
            print(f"El número {num} es impar.")
    elif op == 2:
        fibonacci = [1,1]
        limite = input("Ingrese la cantidad de números de la secuencia Fibonacci que desea ver: ")
        while type(limite) == str:
            try:
                limite = int(limite)
                if limite<1:
                    limite = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")            
            except ValueError:
                limite = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        if limite>2:
            i = 1
            while len(fibonacci)<limite:
                siguiente = fibonacci[i]+fibonacci[i-1]
                fibonacci.append(siguiente)
                i += 1
        print(f"La secuencia Fibonacci de {limite} elementos es:")
        for n in fibonacci:
            print(n)
    else:
        print("Ha salido del programa.")