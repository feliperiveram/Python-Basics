i=1
pos=0
neg=0
cero=0
while i<=5:
    num = input("Ingrese un número entero: ")
    while type(num)==str:
        try:
            num=int(num)
        except ValueError:
            num = input("Valor ingresado no es válido. Ingrese nuevamente un número entero: ")
    if num>0:
        pos=pos+1
    elif num<0:
        neg=neg+1
    else:
        cero=cero+1
    i=i+1
print(f"De los número ingresados {pos} son positivos, {neg} negativos y {cero} son iguales a 0.")