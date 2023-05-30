num = input("Ingrese un número entero: ")
while type(num)==str:
    try:
        num = int(num)
        if num<=0:
            num = input("Número ingresado debe ser positivo (mayor a 0), vuelva a ingresar un número entero: ")
    except ValueError:
        num = input("Número ingresado no válido, vuelva a ingresar un número entero: ")
i=1
sumadiv=0
if num==1:
    print(f"El número {num} no es perfecto.")
else:
    while i<=(num-1):
        division=num%i
        if division==0:
            sumadiv=sumadiv+i
        i=i+1
    if sumadiv==num:
        print(f"El número {num} es perfecto.")
    else:
        print(f"El número {num} no es perfecto.")