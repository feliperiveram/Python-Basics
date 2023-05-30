'''3 enteros e indicar cuántos son menores que 0'''
i=1
conteo=0
while i<=3:
    num = input(f"Ingrese el número entero {i}: ")
    while type(num) == str:
        try:
            num = int(num)
        except ValueError:
            num = input("El valor ingresado no es válido. Ingrese nuevamente un número entero: ")
    if num<0:
        conteo=conteo+1
    i=i+1
print(f"De los números ingresados, {conteo} son menores que 0.")