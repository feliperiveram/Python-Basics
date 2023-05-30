lista = []
x = range(4)
for n in x:
    num = input("Ingrese un número que desee sumar: ")
    while type(num) == str:
        try:
            num = float(num)
        except ValueError:
           num = input("El valor ingresado no es válido. Ingrese nuevamente un número que desee sumar: ")
    lista.append(num)
i = 0
suma = 0
while i<len(lista):
    suma += lista[i]
    i += 1
print(f"La suma de los 4 números ingresados es {suma}.")