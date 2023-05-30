num = input("Ingrese un número del que desee conocer su factorial: ")
while type(num) == str:
    try:
        num = int(num)
        if num<=0:
            num = input("Número debe ser mayor o igual a 0, ingrese nuevamente un número del que desee conocer su factorial: ")
    except ValueError:
        num = input("Número no válido, ingrese nuevamente un número del que desee conocer su factorial: ")
i = 1
factorial = 1
while i<=num:
    factorial = factorial*i
    i += 1
print(f"El factorial de {num} es {factorial}.")