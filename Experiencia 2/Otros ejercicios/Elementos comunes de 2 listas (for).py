lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
comunes = []
for elemento in lista1:
    if elemento in lista2:
        comunes.append(elemento)
print(f"Los elementos comunes entre {lista1} y {lista2} son {comunes}.")