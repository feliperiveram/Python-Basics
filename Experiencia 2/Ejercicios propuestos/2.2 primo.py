num = input("Ingrese un número entero mayor a 0: ")
sumadiv=0
while (type(num)==str):
    try:
        num = int(num)
        if num<=0:
            num = input("El número debe ser positivo. Ingrese nuevamente un número entero mayor a 0: ")
    except ValueError:
        num = input("Número ingresado no es válido. Ingrese nuvemante un número entero mayor a 0: ")
if num==1:
    print(f"El número {num} no es primo.")
else:
    i=1
    while i<=num:
        division=num%i
        if division==0:
            sumadiv=sumadiv+1
        i=i+1
    if sumadiv==2:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")