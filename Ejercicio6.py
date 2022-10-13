#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.



from curses.ascii import islower, isupper


letra = ""
letra = input("Dime una palabra:")

if (letra.isupper() == True):
    print("La palabra está en mayúsculas")
else:
    print("La palabra está en minúsculas")