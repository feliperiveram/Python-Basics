print(" 1.- DOLAR AUSTRALIANO A PESO CHILENO \n 2.- PESO ARGENTINO A PESO CHILENO \n 3.- YEN A PESO CHILENO")
opcion = int(input("Elija una opción: "))
if opcion == 1:
    acambiar = float(input("Ingrese la cantidad de dolares australianos que desee cambiar a pesos chilenos: "))
    valorpesoch = 545.33
    conversion = acambiar*valorpesoch
    print(f"{acambiar} dolares australianos corresponden a {conversion} pesos chilenos")
elif opcion == 2:
    acambiar = float(input("Ingrese la cantidad de pesos argentinos que desee cambiar a pesos chilenos: "))
    valorpesoch = 3.86
    conversion = acambiar*valorpesoch
    print(f"{acambiar} pesos argentinos corresponden a {conversion} pesos chilenos")
else:
    acambiar = float(input("Ingrese la cantidad de yenes que desee cambiar a pesos chilenos: "))
    valorpesoch = 6.14
    conversion = acambiar*valorpesoch
    print(f"{acambiar} yenes corresponden a {conversion} pesos chilenos")