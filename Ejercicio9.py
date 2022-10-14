#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

numero1 = 0
numero2 = 0
numero3 = 0
ListaNumeros = []   
numero1 = (int)(input("Dime un número:\n"))
numero2 = (int)(input("Dime otro número:\n"))
numero3 = (int)(input("Dime otro número:\n"))

ListaNumeros.insert(0, numero1)
ListaNumeros.insert(1, numero2)
ListaNumeros.insert(2, numero3)
ordenados = sorted(ListaNumeros, reverse=True)

print("El orden sería", ordenados)