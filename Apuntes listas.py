# GENERALIDADES
# - LAS LISTAS PUEDEN TENER DISTINTOS TIPOS DE DATOS DENTRO DE ELLAS (NÚMEROS, CARÁCTERES, ETC.), NO ASÍ LOS ARREGLOS

# 1) EXTENDER UNA LISTA YA CREADA
# nombre_lista = [1,2]
# lista.extend([3,4])
# LA NUEVA LISTA nombre_lista ES [1,2,3,4]

# 2) INSERTAR ELEMENTO EN UNA POSICIÓN PARTICULAR
# nombre_lista = [1,2,3,...,n]
# nombre_lista.insert( POSICIÓN EN LA QUE SE INSERTARÁ EL ELEMENTO , ELEMENTO A INSERTAR )

nombre_lista.insert( 2 , 5 )
# LA NUEVA LISTA nombre_lista SERÁ [1,2,5,3,...,n]

# 3) ELIMINAR UN OBJETO DE LA LISTA
# nombre_lista.remove( OBJETO A ELIMINAR )
lista = [3,2,1,3,3,3]
lista.remove(3)
print(lista)
# EL RESULTADO ES [2,1,3,3,3] YA QUE SOLAMENTE SE ELIMINA LA PRIMERA APARICIÓN DEL OBJETO

# 4) FUNCIÓN pop

# 4.1 ELIMINAR ÚLTIMO ELEMENTO DE LA LISTA
# nombre_lista.pop()

# 4.2 ELIMINAR OBJETO EN POSICIÓN ESPECÍFICA
# nombre_lista.pop( POSICIÓN DEL OBJETO QUE SE DESEA ELIMINAR )

# 5) INVERTIR ORDEN DE LA LISTA
# nombre_lista.reverse()

# 6) FUNCIÓN sort

# 6.1 ORDENAR DE MENOR A MAYOR
# nombre_lista.sort()

# 6.2 ORDENAR DE MAYOR A MENOR
# nombre_lista.sort(reverse=True)

# 7) CREAR UNA COPIA DE LA LISTA
# lista_copia = nombre_lista.copy()

# 8) BORRAR ELEMENTOS DE UNA LISTA
# nombre_lista.clear()

# 9) CONTAR UN ELEMENTO n EN UNA LISTA
# contador = nombre_lista.count( ELEMENTO QUE SE DESEA CONTAR )

# 10) FUNCIONES PARA TRABAJAR SOLAMENTE EN CADENAS DE TEXTO

# 10.1 FUNCIÓN upper
# nombre_lista.upper()
# CONVIERTE TODOS LOS CARÁCTERES DE UNA CADENA DE TEXTO A MAYÚSCULA

# 10.2 FUNCIÓN lower
# nombre_lista.lower()
# CONVIERTE TODOS LOS CARÁCTERES DE UNA CADENA DE TEXTO A MINÚSCULA

# 10.3 FUNCIÓN find
# nombre_lista.find( OBJETO A BUSCAR )
# COMO EL OBJETO A BUSCAR ES TEXTO, SE DEBE INTRODUCIR CON " (TEXTO) "
# DEVUELVE LA POSICIÓN DONDE SE UBICA EL OBJETO

# 10.4 FUNCIÓN replace
# nombre_lista.replace ( PARÁMETRO A REEMPLAZAR , LO QUE SE QUIERE INTRODUCIR EN CAMBIO )

# 11) FUNCIÓN split
# LLEVAR CADENA DE TEXTO A UNA LISTA DE CARÁCTERES
# nombre_cadena.split( ELEMENTO SEPARADOR , NÚMERO DE CORTES A EFECTUAR (PUEDE SER 'maxsplit' PARA EL N° MÁXIMO DE DIVISIONES) )

cadena = "Hola, ¿cómo estás?"
lista = cadena.split( "," ) # LA , ES EL ELEMENTO QUE SERÁ EL CORTE DE LA CADENA
print (lista) # ['Hola', ' ¿cómo estás?']

cadena = "Adiós"
lista = cadena.split()
print (lista) # GENERA LA LISTA ['Adiós']