import random
x = range(10)
lista = []
for n in x:
    num = random.randint(1,100)
    lista.append(num)
print(lista)
mayor = lista[0]
menor = lista[0]
i = 1
while i <= (len(lista)-1):
    if mayor < lista[i]:
        mayor = lista[i]
    if menor > lista [i]:
        menor = lista[i]
    i += 1
print(f"De tal lista, el mayor es {mayor} y el menor es {menor}.")