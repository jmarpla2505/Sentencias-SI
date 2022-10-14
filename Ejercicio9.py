#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

numero1 = 0
numero2 = 0
numero3 = 0
numero1 = int(input("Dime un número:"))
numero2 = int(input("Dime otro número:"))
numero3 = int(input("Dime un tercer número:"))

if (numero1>numero2>numero3):
    print(numero1,numero2,numero3)
elif (numero2>numero1>numero3):
    print(numero2,numero1,numero3)
elif (numero3>numero1>numero2):
    print(numero3,numero1,numero3)
elif (numero1>numero3>numero2):
    print(numero1,numero3,numero2)
elif (numero2>numero3>numero1):
    print(numero2,numero3,numero1)
elif (numero3>numero2>numero1):
    print(numero3,numero2,numero1)