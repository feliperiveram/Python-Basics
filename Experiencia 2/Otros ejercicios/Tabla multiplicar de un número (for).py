menu = 1
while menu != 2:
    num = input("Ingrese el número del que desee conocer su tabla de multiplicación: ")
    while type(num) == str:
        try:
            num = float(num)
        except ValueError:
            num = input("Valor no válido, ingrese nuevamente su opción: ")
    limite = input("Ingrese el número hasta el cual desee multiplicar el número anteriormente ingresado: ")
    while type(limite) == str:
        try:
            limite = int(limite)
        except ValueError:
            limite = input("Valor no válido, ingrese nuevamente su opción: ")
    for elemento in range(1,limite+1,1):
        print(f"{num}*{elemento}={num*elemento}")
    # Menú y validador de número ingresado
    print("1.- VISUALIZAR OTRA TABLA DE MULTIPLICAR \n2.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("Valor no válido, ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor no válido, ingrese nuevamente su opción: ")