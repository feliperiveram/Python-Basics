menu = 1
while menu != 2:
    suma = 0
    num = input("Ingrese un número del cual desee conocer su sumatoria: ")
    while type(num) == str:
        try:
            num = int(num)
            if num <= 0:
                num = input("El valor ingresado no es válido, ya que este debe ser mayor o igual a 1. Ingrese nuevamente un número hasta el que desee contar: ") 
        except ValueError:
            num = input("El valor ingresado no es válido. Ingrese nuevamente un número hasta el que desee contar: ")
    i=1
    if num==1:
        print(f"La sumatoria es {1}.")
    else:
        while i <= num:
            suma = suma+i
            i += 1
        print(f"La sumatoria es {suma}.")
    print("1.- REALIZAR SUMATORIA DE OTRO NÚMERO\n2.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("El valor ingresado no es válido. Ingrese nuevamente su opción: ") 
        except ValueError:
            menu = input("El valor ingresado no es válido. Ingrese nuevamente su opción: ")