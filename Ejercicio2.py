#Algoritmo que pida un número y diga si es positivo, negativo o 0.
numero = (int)(input("Dime un número:\n"))
if numero==0:
    print("El número es igual a 0")
else:
    if numero<0:
        print("El número es negativo")
    else:
        print("El número es positivo")