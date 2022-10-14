"""
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
circunferencias y las clasifique en uno de estos estados:
 exteriores
 tangentes exteriores
 secantes
 tangentes interiores
 interiores
 concéntricas
"""

import math

x1 = (int)(input("Dime la coordenada x1:\n"))
y1 = (int)(input("Dime la coordenada y1:\n"))
r1 = (int)(input("Dime el radio r1:\n"))
x2 = (int)(input("Dime la coordenada x2:\n"))
y2 = (int)(input("Dime la coordenada y2:\n"))
r2 = (int)(input("Dime el radio r2:\n"))

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

if distancia > (r1 + r2):
    print("Las circunferencias son exteriores")
if distancia == (r1 + r2):
    print("Las circunferencias son tangentes exteriores")
if (distancia < (r1 + r2) and distancia > abs(r1-r2)):
    print("Las circunferencias son secantes")
if distancia == abs(r1-r2):
    print("Las circunferencias son tangentes interiores")
if (distancia < abs(r1-r2) and distancia > 0):
    print("Las circunferencias son interiores")
if distancia == 0:
    print("Las circunferencias son concéntricas")  