'''Ingresar por teclado 5 números enteros, luego debe indicar:
• Cuántos números son mayores a cero
• Sume los números pares
• Mostrar los resultados'''
i = 1
positivos = 0
sumapar = 0
while i<=5:
    num = input(f"Ingrese el número entero {i}/5: ")
    while type(num) == str:
        try:
            num = int(num)
        except ValueError:
            num = input(f"El número ingresado no es válido, ingrese nuevamente el número entero {i}/5: ")
    if num>0:
        positivos += 1
    if num%2==0:
        sumapar += num
    i += 1
print(f"{positivos} números son mayores que cero y la suma de los números pares es {sumapar}.")