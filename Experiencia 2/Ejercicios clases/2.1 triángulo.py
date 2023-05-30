'''Ingresar 3 ángulos e indicar tipo de triángulo'''
a1=input("Ingrese el primer ángulo: ")
while type(a1) == str:
    try:
        a1 = float(a1)
    except ValueError:
        a1=input("El valor ingresado no es válido. Ingrese nuevamente el primer ángulo: ")
a2=input("Ingrese el segundo ángulo: ")
while type(a2) == str:
    try:
        a2 = float(a2)
    except ValueError:
        a2=input("El valor ingresado no es válido. Ingrese nuevamente el segundo ángulo: ")
a3=input("Ingrese el tercer ángulo: ")
while type(a3) == str:
    try:
        a3 = float(a3)
    except ValueError:
        a3=input("El valor ingresado no es válido. Ingrese nuevamente el primer ángulo: ")
if (a1==a2) and (a2==a3):
    print("Es equilátero.")
elif (a1==a2) or (a1==a3) or (a2==a3):
    print("Es isósceles.")
else:
    print("Es escaleno.")
