# Funciones
# IVA
def calculo_iva(precio_producto):
    valor_iva = precio_producto*0.19
    return valor_iva #Retorna el valor del IVA del producto. Requiere tener el valor del unitario del producto

# DESCUENTO
def precio_final(valor_producto,descuento):
    precio_final = round(valor_producto-(descuento/100)*valor_producto)
    return precio_final

# CALCULAR IMC
def calculo_imc(peso,altura):
    imc = (peso)/(altura**2)
    return imc

#Programa
menu = 0
print("¡Bienvenid@! ¿Qué deseas realizar?:\n1.- CALCULAR IVA\n2.- DESCUENTO\n3.- CALCULAR IMC\n4.- SALIR DEL PROGRAMA")
while menu != 4:
    menu = int(input("Ingrese su opción: "))
    if menu == 1:
        precio = int(input("Ingrese el valor del producto del que desea conocer su IVA: "))
        print(f"El IVA del producto es ${calculo_iva(precio)}.")
    elif menu == 2:
        precio = int(input("Ingrese el valor unitario del producto al que le desea aplicar un descuento: $"))
        descuento = float(input("Ingrese el descuento que le quiere aplicar al producto: "))
        print(f"El precio final del producto es {precio_final(precio,descuento)} ya que aplicó el {descuento}% de descuento.")
    elif menu == 3:
        peso = float(input("Ingrese su peso: "))
        altura = float(input("Ingrese su altura: "))
        print(f"Su IMC es {calculo_imc(peso, altura)}")
        if calculo_imc(peso, altura) < 18.5:
            print("Usted se encuentra bajo peso.")
        elif (calculo_imc(peso, altura) >= 18.5) or (calculo_imc(peso, altura) <= 24.9):
            print("Usted se encuentra en un peso adecuado.")
        elif (calculo_imc(peso, altura) >= 25) or (calculo_imc(peso, altura) <= 29.9):
            print("Usted se encuentra con sobrepeso.")
        elif (calculo_imc(peso, altura) >= 30) or (calculo_imc(peso, altura) <= 34.9):
            print("Usted se encuentra con obesidad grado I.")
        elif (calculo_imc(peso, altura) >= 35) or (calculo_imc(peso, altura) <= 39.9):
            print("Usted se encuentra con obesidad grado II.")
        else:
            print("Usted se encuentra con obesidad grado III.")
    else:
        print("¡Gracias por haber usado el programa!")