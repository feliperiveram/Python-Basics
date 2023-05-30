num = input("Ingrese un número hasta el que desee contar: ")
while type(num) == str:
    try:
        num = int(num)
        if num <= 0:
            num = input("El valor ingresado no es válido, ya que este debe ser mayor o igual a 1. Ingrese nuevamente un número hasta el que desee contar: ") 
    except ValueError:
        num = input("El valor ingresado no es válido. Ingrese nuevamente un número hasta el que desee contar: ")
i=1
while i <= num:
    print(i)
    i += 1