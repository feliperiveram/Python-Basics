palabra = input("Ingrese su palabra: ")
vocales = "aeiouAEIOU"
contar = 0
for letra in palabra:
    if letra in vocales:
        contar += 1
print(f"El número de vocales en '{palabra}' es de {contar}.")