i = 1
suma = 0
num = input("Ingrese un número hasta el que desea contar, este debe ser mayor o igual a 1: ")
while type(num) == str:
    try:
        num = int(num)
        if num<1:
            num = input("El valor ingresado no es válido, ingrese otro número hasta el que desee sumar: ")
    except ValueError:
        num = input("El valor ingresado no es válido, ingrese otro número hasta el que desee sumar: ")
while i<=num:
    suma += i
    i +=1
print(f"La suma de los número naturales hasta el {num} es {suma}.")