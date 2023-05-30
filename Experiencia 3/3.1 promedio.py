x = range(10)
lista = []
suma = 0
conteo = 0
for n in x:
    num = float(input("Ingrese el número: "))
    lista.append(num)
i = 0
while i <= (len(lista)-1):
    suma += lista[i]
    i += 1
    conteo += 1
print(f"La suma de los elementos es {suma} y el promedio es {suma/conteo}")