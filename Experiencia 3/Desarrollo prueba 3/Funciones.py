# Listas iniciales
lista_nif_num = []
lista_nif_char = []
lista_nif = []
lista_nombres = []
lista_edades = []

# Funciones
def grabar():
    nif_num = input("Ingrese la parte numérica del NIF a crear (8 dígitos): ")
    while (len(nif_num) != 8) or ((int(nif_num)) == ValueError):
        nif_num = input("Dígitos ingresados no son válidos. Ingrese nuevamente la parte numérica del NIF a crear (8 dígitos): ")
    nif_char = input("Ingrese la parte alfabética del NIF a crear (3 carácteres): ")
    while (len(nif_char) != 3):
        nif_char = input("Deben ser solo 3 carácteres. Ingrese nuevamente la parte alfabética del NIF a crear (3 carácteres): ")
    nif_char = nif_char.upper()
    nif_nuevo = nif_num+"-"+nif_char
    if nif_nuevo not in lista_nif:
        nombre = input(f"Ingrese el nombre (al menos 8 carácteres) de la persona de NIF {nif_nuevo}: ")
        while (len(nombre) < 8):
            nombre = input(f"Nombre ingresado no es válido. Ingrese nuevamente el nombre (al menos 8 carácteres) de la persona de NIF {nif_nuevo}: ")
        edad = input(f"Ingrese la edad de la persona de NIF {nif_nuevo}: ")
        while type(edad) == str:
            try:
                edad = int(edad)
                if edad < 0:
                    edad = input(f"La edad debe ser mayor o igual a 0. Ingrese nuevamente la edad de la persona de NIF {nif_nuevo}: ")
            except ValueError:
                edad = input(f"Valor ingresado no es válido. Ingrese nuevamente la edad de la persona de NIF {nif_nuevo}: ")
        if edad > 15:
            print("Proceso finalizado correctamente.")
            lista_nif_num.append(nif_num)
            lista_nif_char.append(nif_char)
            lista_nif.append(nif_nuevo)
            lista_nombres.append(nombre)
            lista_edades.append(edad)
        else:
            print("La persona debe ser mayor a 15 años para que le sea entregado un NIF.")
    else:
        print(f"El NIF {nif_nuevo} ya ha sido ingresado anteriormente.")

# Persona pertenece a la Unión Europea si su NIF termina en UNE
def buscar():
    nif = input("Ingrese el NIF a buscar (formato: 11111111-ABC): ")
    nif = nif.upper()
    if nif in lista_nif:
        i = 0
        while i <= (len(lista_nif) - 1):
            if nif == lista_nif[i]:
                posicion = i
            i += 1
        print(f"Nombre: {lista_nombres[posicion]}\nNIF: {nif}\nEdad: {lista_edades[posicion]}")
        if lista_nif_char[posicion] == "UNE":
            print("Persona pertenece a la Unión Europea.")
    else:
        print(f"El NIF {nif} no ha sido ingresado anteriormente.")

# Nacimiento, estado conyugal, pertenencia a la UNE
def imprimir_certificado():
    nif = input("Ingrese el NIF del que desea obtener algún certificado (formato: 11111111-ABC): ")
    nif = nif.upper()
    if nif in lista_nif:
        print("¿Qué certificado desea?:\n1.- NACIMIENTO\n2.- ESTADO CONYUGAL\n3.- PERTENENCIA A LA UNIÓN EUROPEA")
        opcion = input("Ingrese su opción: ")
        while type(opcion) == str:
            try:
                opcion = int(opcion)
                if opcion > 3 or opcion < 1:
                    opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
            except ValueError:
                opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        i = 0
        while i <= (len(lista_nif) - 1):
            if nif == lista_nif[i]:
                posicion = i
            i += 1
        if opcion == 1:
            print("CERTIFICADO DE NACIMIENTO\n___________________________")
            print(f"Nombre: {lista_nombres[posicion]}\nNIF: {nif}\nFecha de nacimiento: XX/XX/XXXX\nEdad: {lista_edades[posicion]}")
        elif opcion == 2:
            print("CERTIFICADO DE ESTADO CIVIL\n___________________________")
            print(f"Nombre: {lista_nombres[posicion]}\nNIF: {nif}\nEstado civil: XXXXXXXXX\nEdad: {lista_edades[posicion]}")
        else:
            print("CERTIFICADO DE PERTENENCIA A LA UNIÓN EUROPEA\n___________________________")
            print(f"Nombre: {lista_nombres[posicion]}\nNIF: {nif}\nEdad: {lista_edades[posicion]}")
            if lista_nif_char[posicion] == "UNE":
                print("Pertenencia a la Unión Europea: SÍ")
            else:
                print("Pertenencia a la Unión Europea: NO")
    else:
        print(f"El NIF {nif} no se encuentra en nuestros registros.")