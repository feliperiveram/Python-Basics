cant=input("Ingrese el número de pares de zapatos que quiere: ")
while type(cant) == str:
    try:
        cant = int(cant)
    except ValueError:
        cant = input("Opción inválida. Ingres nuevamente su opción: ")
while cant<=0:
    cant=input("Debe ser un valor mayor que 0. Ingrese el número de pares de zapatos que quiere: ")
    while type(cant) == str:
        try:
            cant = int(cant)
        except ValueError:
            cant = input("Opción inválida. Ingres nuevamente su opción: ")
total = cant*20000
envio = 3000
if total>=40000:
    print(f"Debe pagar ${total} por su compra.")
else:
    print(f"Debe pagar ${total+envio}.")