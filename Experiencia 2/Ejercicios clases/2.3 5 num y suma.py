'''Ingrese por teclado 5 números enteros positivos, súmelos y muestre el resultado de la suma.'''
i = 1
suma = 0
while i<=5:
    num = input(f"Ingrese el número entero positivo {i}/5: ")
    while type(num) == str:
        try:
            num = int(num)
            if num<=0:
                num = input(f"El número debe ser un entero positivo, ingrese nuevamente el número entero {i}/5: ")
        except ValueError:
            num = input(f"El número ingresado no es válido, ingrese nuevamente el número entero positivo {i}/5: ")
    suma += num
    i += 1
print(f"El resultado de la suma es {suma}.")