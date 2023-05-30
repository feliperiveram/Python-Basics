num1 = input("Ingrese el primer número: ")
while type(num1) == str:
    try:
        num1 = float(num1)
    except ValueError:
        num1 = input("El dato es erróneo, vuelva a ingresar número 1: ")
num2 = input("Ingrese el segundo número: ")
while type(num2) == str:
    try:
        num2 = float(num2)
    except ValueError:
        num2 = input("El dato es erróneo, vuelva a ingresar número 2: ")
suma = num1+num2
print(f"La suma de los dos números es: {suma}")