lista = []
menu = 1
while menu != 2:
    num = input("Introduzca un número a la lista: ")
    while type(num) == str:
        try:
            num = float(num)
        except ValueError:
            num = input("Valor no válido, agregue un número a la lista: ")
    lista.append(num)
    print("1.- AGREGAR OTRO NÚMERO \n2.- ENCONTRAR EL VALOR MÁXIMO DE LOS NÚMEROS INGRESADOS")
    menu = input("Seleccione su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("Valor no válido, seleccione nuevamente su opción: ")
        except ValueError:
            menu = input("Valor no válido, seleccione nuevamente su opción: ")
maximo = lista[0]
for elemento in lista:
    if elemento>maximo:
        maximo = elemento
print(f"El número mayor de {lista} es {maximo}.")