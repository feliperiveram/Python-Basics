i=1
suma=0
conteo=0
while i<=3:
    num = int(input(f"Ingrese el número entero {i}: "))
    if (num>0) and (num%2 == 0):
        suma=suma+num
    else:
        conteo=conteo+1
    i=i+1
print(f"Suma de los números mayores a 0 y pares = {suma}.")
print(f"Cantidad de número que no cumplen ambas condiciones anteriores = {conteo}.")