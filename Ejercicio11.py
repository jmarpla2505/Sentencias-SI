""" Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las
dimensiones de los lados de un triángulo. El programa debe determinar que tipo
de triangulo es, teniendo en cuenta los siguiente:
 Si se cumple Pitágoras entonces es triángulo rectángulo
 Si sólo dos lados del triángulo son iguales entonces es isósceles.
 Si los 3 lados son iguales entonces es equilátero.
 Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""
import math
A = 0
B = 0
C = 0

A = int(input("Dime A:\n"))
B = int(input("Dime B:\n"))
C = int(input("Dime C:\n"))

if (C==math.sqrt(B**2+A**2)):
    print("Es un triángulo rectángulo")
elif (A==B==C):
    print("El triángulo es equilátero")
else:
    print("Es escaleno")
