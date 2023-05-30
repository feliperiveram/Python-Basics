num = int(input("Ingrese un número: "))
lista = []
i = 1
while i <= 10:
    multiplo = num*i
    lista.append(multiplo)
    i += 1
print(f"La lista que usted ingresó es: {lista}")
print(f"La lista ascendente es: {lista}")
lista.sort(reverse=True)
print(f"La lista en orden descendente es: {lista}")