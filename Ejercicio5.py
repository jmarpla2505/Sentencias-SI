#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha
#introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un
#error.

usuSecreto="Pepe"
passSecreto="asdasd"
usuario = input("Dime tu usuario: ")
contrasena= input("Dime tu contraseña: ")

while (usuSecreto!=usuario or passSecreto!=contrasena) :
 if(usuSecreto!=usuario) :
    print("Error en el ususario") 
    usuario = input("Dime tu usuario: ")
 elif (passSecreto!=contrasena):
    print("Error en la contraseña") 
    usuario = input("Dime tu contraseña: ")

print("Usuario y Contraseña correctos")