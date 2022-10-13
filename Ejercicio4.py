#Crea un programa que pida al usuario dos números y muestre su división si el
#segundo no es cero, o un mensaje de aviso en caso contrario.

numero1 = 0
numero2 = 0
numero1 = int(input("Dime un número:"))
numero2 = int(input("Dime otro número"))
if (numero2 == 0):
    print("El segundo número no puede ser cero")
else:
    print("La división del los número es:", numero1/numero2)
