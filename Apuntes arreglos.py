# SIEMPRE INCLUIR import numpy as np AL COMIENZO
import numpy as np

# GENERALIDADES
# - LAS POSICIONES VAN DE 0 A (len(nombre_arreglo)-1)
# - LA POSICIÓN nombre_arreglo[-1] ES EL ÚLTIMO ELEMENTO DEL ARREGLO

# ARREGLOS UNIDIMENSIONALES

# 1) CREAR UNA MATRIZ DE CIERTA CANTIDAD DE ELEMENTOS ALEATORIOS
# NO REQUIERE IMPORTAR random AL COMIENZO
# nombre_arreglo = np.random.randint(ELEMENTO INICIAL , ELEMENTO MÁXIMO (SIN INCLUIR) , size=(CANTIDAD DE ELEMENTOS DEL ARREGLO))

arreglo = np.random.randint(1,101,size=(10))
# EL ARREGLO 'arreglo' ES UNA MATRIZ UNIDIMENSIONAL DE 10 ELEMENTOS, LOS CUALES SON ALEATORIOS Y PUEDEN TOMAR VALORES DEL 1 AL 101
# (INCLUYENDO AL 1 PERO EXCLUYENDO AL 101, ES DECIR TOMA LOS VALORES ENTRE 1 Y 100)

# 2) CREAR UNA MATRIZ DE CANTIDAD VARIABLE DE ELEMENTOS SEGÚN PARÁMETROS ESTABLECIDOS
# nombre_arreglo = np.arange(VALOR INICIAL , VALOR MÁXIMO (SIN INCLUIR) , STEP)
# LARGO DE ARREGLO DEPENDE DE LOS PARÁMETROS INGRESADOS

arreglo = np.arange(1,102,10)
# GENERA EL SIGUIENTE ARREGLO: [  1  11  21  31  41  51  61  71  81  91 101  ] (11 ELEMENTOS)

arreglo = np.arange(1,101,10)
# GENERA EL SIGUIENTE ARREGLO: [  1  11  21  31  41  51  61  71  81  91  ] (10 ELEMENTOS)

nombre_arreglo = np.arange(4)
# GENERA EL SIGUIENTE ARREGLO: [  0  1  2  3  ] (4 ELEMENTOS QUE VAN DESDE EL 0 AL 3)

nombre_arreglo = np.arange(4.)
# GENERA EL SIGUIENTE ARREGLO: [  0.  1.  2.  3.  ] (4 ELEMENTOS DECIMALES QUE VAN DESDE EL 0. AL 3.)

# 3) OPERACIONES BÁSICAS

# 3.1 SUMA DE ELEMENTOS DEL ARREGLO
# nombre_arreglo.sum()
print (f"La suma de los elementos del arreglo es {arreglo.sum()}.")

# 3.2 PROMEDIO
# nombre_arreglo.mean()

# 3.3 SUMAR TODOS LOS ELEMENTOS DE UN ARREGLO POR ALGUNA CONSTANTE
# nombre_arreglo += n
arreglo += 5
# DEVUELVE EL ARREGLO CON TODOS SUS ELEMENTOS ORIGINALES AUMENTADOS EN 5

# 3.4 USO DE POTENCIAS
# nombre_arreglo **= n
arreglo **= 2
# DEVUELVE EL ARREGLO CON TODOS LOS CUADRADOS DE SUS ELEMENTOS ORIGINALES

# 3.5 OPERACIONES ENTRE ARREGLOS

# 3.5.1
# ARREGLOS SE PUEDEN OPERAR ENTRE SÍ (SUMA ELEMENTO A ELEMENTOS, DIVISIÓN ELEMENTO A ELEMENTO, ETC.)
# arreglo_resultante = nombre_arreglo_1 (+,-,/,*) nombre_arreglo_2

# 3.5.2
# ARREGLOS SE PUEDEN COMPARAR ENTRE SÍ -> DEVUELVE ARREGLO BOOLEANO
# arreglo_comparacion = nombre_arreglo_1 (==,>,<,etc.) nombre_arreglo_2

# 3.6 ENCONTRAR EL VALOR MÁXIMO O MÍNIMO DE UN ARREGLO
# nombre_arreglo.max() Y nombre_arreglo.min()

# 4) CREACIÓN DE UN ARREGLO

# 4.1 A PARTIR DE UNA LISTA YA CREADA
# SI EXISTE nombre_lista = [1,2,3,...,n]
# SE PUEDE USAR nombre_arreglo = np.array(nombre_lista)

# 4.2 DIRECTAMENTE CON FUNCIÓN DE NUMPY
# nombre_arreglo = np.array([1,2,3,...,n])

# 4.3 CON FUNCIÓN i for i in range(n) PARA CREAR UNA LISTA (Y LUEGO CREAR EL ARREGLO DE TAL LISTA)
# nombre_lista = [i for i in range(DESDE DONDE , HASTA DONDE (SIN INCLUIR)) , STEP OPCIONAL]

lista = [i for i in range(1,11)]
# DEVUELVE UNA LISTA CON 10 ELEMENTOS ([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10])

# 5) MOSTRAR DIMENSIONES DE UN ARREGLO (SIRVE PARA UNI Y BIDIMENSIONALES)
# print(nombre_arreglo.ndim)
# DEVUELVE EL NÚMERO DE DIMENSIONES

# 6) MOSTRAR LARGO DE UN ARREGLO
# print(len(nombre_arreglo))

# 7) SLICE
# nombre_arreglo[DESDE DONDE : HASTA DONDE (SIN INCLUIR) : STEP OPCIONAL]; LOS PARÁMETROS SON EN BASE A LAS POSICIONES DE LOS ELEMENTOS
# LAS POSICIONES VAN DE 0 A (len(nombre_arreglo)-1)

# 8) COPIAR ARREGLOS

# 8.1 COPIAR Y MODIFICAR AMBOS ARREGLOS (DOS ARREGLOS "UNIFICADOS") -> CAMBIOS EN UN ARREGLO SE REFLEJAN TAMBIÉN EN EL OTRO
# arreglo_copia = nombre_arreglo[:]

# 8.2 COPIAR Y CREAR 2 ARREGLOS INDEPENDIENTES ENTRE SÍ
# arreglo_copia = nombre_arreglo[].copy()

# 9) CREAR ARREGLOS LLENOS DE 1'S
# nombre_arreglo = np.ones(4) -> GENERA ARREGLO DE 4 ELEMENTOS, LOS CUALES SON TODOS IGUALES A 1

# ARREGLOS BIDIMENSIONALES

# 1) CREACIÓN DE UN ARREGLO

# 1.1 TRADICIONAL
nombre_arreglo = np.array( [ [0,1,2] , [3,4,5] ] )

# 1.2 USANDO LISTAS
# nombre_lista = [ [0,1,2] , [3,4,5] ]
# nombre_arreglo = np.array(nombre_lista)

# 1.3 MATRIZ CON ELEMENTOS ALEATORIOS
# nombre_arreglo = np.random.randint( VALOR MÍNIMO , VALOR MÁXIMO SIN INCLUIR , size = ( VERTICAL , HORIZONTAL ))
# NO REQUIERE IMPORTAR random

nombre_arreglo = np.random.randint( 1 , 20 , size=(3,3) )
# GENERA MATRIZ 3X3 CON ELEMENTOS ALEATORIOS QUE TOMAN LOS VALORES ENTRE 1 Y 19. PUDIENDO TOMAR EL VALOR DE 1 Y 19

# 2) MOSTRAR ELEMENTO DE MATRIZ
# nombre_arreglo[NÚMERO DE POSICIÓN EN EJE VERTICAL][NÚMERO DE POSICIÓN EN EJE HORIZONTAL]

# 3) MOSTRAR TODOS LOS ELEMENTOS DE LA MATRIZ

nombre_arreglo = np.array( [ [0,1,2] , [3,4,5] ] )
# MATRIZ DE 3X2, POR LO QUE EN EL EJE VERTICAL TIENE 2 ELEMENTOS Y EN EL HORIZONTAL 3
for n in range(2):
# EN EL PRIMER for VA EL EJE VERTICAL
    for m in range(3):
    # EN EL SEGUNDO for VA EL EJE HORIZONTAL
        print(nombre_arreglo[n][m])
        
# 4) SLICE

# 4.1 USO TRADICIONAL
# nombre_arreglo[ PARTE VERTICAL A MOSTRAR , PARTE HORIZONTALA MOSTRAR ]
# EN PARÁMETROS VAN LAS POSICIONES (MENOS STEP)
# SI STEP ES NEGATIVO SE INVIERTE
# nombre_arreglo[ DESDE DONDE : HASTA DONDE (EXCLUYÉNDOLO) : STEP OPCIONAL , DESDE DONDE : HASTA DONDE (EXCLUYÉNDOLO) : STEP OPCIONAL ]

# 4.2 MOSTRAR SOLO 1 FILA
# nombre_arreglo[ POSICIÓN DE NÚMERO DE FILA A MOSTRAR , : ]

nombre_arreglo[ 0 , : ]
# MUESTRA FILA NÚMERO 1

nombre_arreglo[ 0 , : ].sum()
# MUESTRA SUMA DE LOS ELEMENTOS DE LA FILA NÚMERO 1

# 4.2 MOSTRAR SOLO 1 COLUMNA EN FORMA VERTICAL
# nombre_arreglo[  :  , m : m+1 : ]
# COLUMNA 1 -> m = 0
# COLUMNA 2 -> m = 1

# 4.3 MOSTRAR SOLO 1 COLUMNA EN FORMA HORIZONTAL
# nombre_arreglo[  :  , m ]
# COLUMNA 1 -> m = 0
# COLUMNA 2 -> m = 1

# 5) MOSTRAR CANTIDAD DE ELEMENTOS
# nombre_arreglo.size
# EN SIZE NO SE DEBE INCLUIR '( )' (ESTARÍA MAL ESCRIBIR nombre_arreglo.size())

# 6) CONCATENAR (UNIR) MATRICES

# DADAS LAS MATRICES YA CREADAS nombre_arreglo_1 y nombre_arreglo_2

# 6.1 EN FORMA VERTICAL (HACIA ABAJO)
# np.concatenate (( nombre_arreglo_1 , nombre_arreglo_2 ), axis = 0 )

# 6.2 EN FORMA HORIZONTAL (HACIA EL LADO)
# np.concatenate (( nombre_arreglo_1 , nombre_arreglo_2 ), axis = 1 )

# 7) SABER CARDINALIDAD DE LA MATRIZ
# nombre_arreglo.shape

# 8) GENERAR MATRIZ CON 0'S
# nombre_arreglo = np.zeros((3,3)) -> GENERAR MATRIZ 3X3 LLENA DE CEROS

# 9) GENERAR MATRIZ CON 1'S
# nombre_arreglo = np.ones((3,3)) -> GENERAR MATRIZ 3X3 LLENA DE UNOS

# 10) GENERAR MATRIZ CON DIAGONAL PRINCIPAL CON 1'S
# nombre_arreglo = np.diag([1,1,1]) -> GENERAR MATRIZ 3X3 CON ELEMENTOS EN LA DIAGONAL PRINCIPAL IGUALES A 1. EL RESTO DE ELEMENTOS SON CEROS (0'S)

# 11) LLEVAR ARREGLO UNIDIMENSIONAL A UNO BIDIMENSIONAL
# .reshape( VERTICAL , HORIZONTAL )
# nombre_arreglo = np.arange(1,101) -> GENERA ARREGLO UNIDIMENSIONAL CON 100 ELEMENTOS (1 AL 100)
# nombre_arreglo = np.arange(1,101).reshape(10,10) -> GENERA ARREGLO BIDIMENSIONAL 10X10 CON 100 ELEMENTOS (1 AL 100)

# 12) CREAR UNA MATRIZ QUE SELECCIONE ELEMENTOS ALEATORIOS DE UNA LISTA YA CREADA

import string

abecedario = list(string.ascii_lowercase)

# nombre_arreglo = np.random.choice( NOMBRE DE LISTA , size=( VERTICAL , HORIZONTAL ) )
nombre_arreglo = np.random.choice(abecedario,size=(4,4))
# SE CREA MATRIZ 4X4 CON 16 ELEMENTOS ALEATORIOS PERTENECIENTES A LA LISTA 'abecedario'

# 12) Crear matriz con números reales (decimales)

# arreglo = np.random.uniform(1,10,(TAMAÑO EN eje_y,TAMAÑO EN eje_x)) -> elementos pueden tomar el valor de 1 y 10

# 13) OTROS

# arreglo = np.arange(1, 43)
# arreglo_str = [str(i).zfill(2) for i in arreglo]
# avion_original = np.array(arreglo_str).reshape(7,6)
# asientos_disponibles = avion_original[:].copy()