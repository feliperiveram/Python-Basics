# Sin argumento y sin retorno
def saludo():
    print("Hola")
saludo()

lista = [10,50,100,500,1000,5000]
def listar():
    for n in range(len(lista)):
        print(lista[n])

listar()

# Sin argumento y con retorno
def sumar():
    num1 = 3
    num2 = 5
    return(num1 + num2) # Devuelve alguna variable
print(f"La suma es {sumar()}")

def sumar_lista():
    suma = 0
    for n in range(len(lista)):
        suma += lista[n]
    return suma
print(f"La suma de los elementos de la lista es: {sumar_lista()}")

# Otra forma:
# for n in lista:
#     suma += n           -> n toma todos los valores de cada elemento de la lista


# Con argumento y sin retorno
def sumar(a,b): # Argumentos de la función -> Pide información
    suma = a + b
    print(f"La suma de los elementos es {suma}.")

num1 = int(input("Ingrese un valor a sumar: "))
num2 = int(input("Ingrese un valor a sumar: "))
sumar (num1,num2)

# Con argumento y con retorno
def sumar(a,b):
    suma = a+b
    return(suma)
num1 = int(input("Ingrese un valor a sumar: "))
num2 = int(input("Ingrese un valor a sumar: "))
print(f"La suma de los números es {sumar(num1,num2)}.")

'''
Llamar a funciones personalizadas en otro archivo

En nuevo archivo en misma carpeta -> import (nombre archivo) as ____
En nuevo archivo en otra carpeta -> import (nombre carpeta).(nombre archivo) as ____
'''