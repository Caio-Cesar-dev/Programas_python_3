"""Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo. Calcule e mostre o comprimento da hipotenusa."""
#OUTRA FORMA DE FAZER IMPORTANDO APENAS O METODO 'HIPOT'
#from math import  hypot
"""co=float(input("cateto oposto: "))
ca=float(input("cateto adjacente: "))
hi=hypot(co,ca)

print("A hipotenusa vai medir {:.2f}".format(hi))"""

co=float(input("cateto oposto: "))
ca=float(input("cateto adjacente: "))

hi=((co**2)+(ca**2))**0.5
print("A hipotenusa vai medir {:.2f}".format(hi))

