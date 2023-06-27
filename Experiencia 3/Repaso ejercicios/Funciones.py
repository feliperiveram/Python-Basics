# Listas iniciales
lista_numero_partes = []
lista_nombres = []
lista_precios = []

def grabar():
    numero_parte = input("Ingrese el número de parte: ")
    while len(numero_parte) < 10:
        numero_parte = input("Número de partes debe tener al menos 10 carácteres. Ingrese nuevamente el número de partes: ")
    numero_parte = numero_parte.upper()
    if numero_parte not in lista_numero_partes:
        nombre = input(f"Ingrese el nombre del componente {numero_parte}: ")
        while len(nombre) < 6:
            nombre = input("Nombre debe tener al menos 6 carácteres. Ingrese nuevamente el nombre: ")
        precio = input(f"Ingrese el precio del componente {numero_parte}: $")
        while type(precio) == str:
            try:
                precio = int(precio)
                if precio <= 0:
                    precio = input("Precio debe ser mayor a $0. Ingrese nuevamente el precio: $")
            except ValueError:
                precio = input("Valor ingresado no es válido. Ingrese nuevamente el precio: $")
        lista_nombres.append(nombre)
        lista_numero_partes.append(numero_parte)
        lista_precios.append(precio)
        print(f"Componente {numero_parte} correctamente guardado.")
    else:
        print("Número de partes ya ha sido ingresado anteriormente.")

def buscar():
    numero_parte = input("Ingrese el número de partes del componente que desea buscar: ")
    numero_parte = numero_parte.upper()
    if numero_parte in lista_numero_partes:
        i = 0
        while i <= (len(lista_numero_partes) - 1):
            if numero_parte == lista_numero_partes[i]:
                posicion = i
            i += 1
        if lista_precios[posicion] >= 500:
            print("DETALLE DE COMPONENTE\n________________________\n")
            print(f"Nombre: {lista_nombres[posicion]}")
            print(f"Número de partes: {lista_numero_partes[posicion]}")
            print(f"Precio: ${lista_precios[posicion]}")
            print("________________________\n")
        else:
            print("Producto sin stock.")
    else:
        print(f"Número de partes {numero_parte} no ha sido ingresado anteriormente.")

def imprimir():
    if len(lista_nombres) != 0:
        print("DETALLE DE COMPONENTES\n________________________\n")
        i = 0
        while i <= (len(lista_nombres) - 1):
            print(f"Nombre: {lista_nombres[i]}")
            print(f"Número de partes: {lista_numero_partes[i]}")
            print(f"Precio: ${lista_precios[i]}")
            i += 1
        print("________________________\n")
    else:
        print("No hay ningún componente guardado en el programa.")