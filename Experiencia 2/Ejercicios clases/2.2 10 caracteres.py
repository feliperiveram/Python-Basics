i=1
vocales=0
consonantes=0
letrasvocales="aeiou"
while i <= 10:
    caracter = input("Ingrese un caracter: ")
    if caracter in letrasvocales:
        vocales=vocales+1
    i=i+1
print(f"De los carácteres ingresados, {vocales} son vocales y {10-vocales} son consonantes.")