num=1
divisor=1
while num<10:
    if num%2==0:
        print(f"Tabla de multiplicar del {num}.")
        while divisor<=10:
            print(f"{num}*{divisor}={num*divisor}")
            divisor=divisor+1
    divisor=1
    num=num+1