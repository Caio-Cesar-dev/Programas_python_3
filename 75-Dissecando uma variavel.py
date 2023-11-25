"""Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
 informações possíveis sobre ele."""
a=input('Digite algo: ')
print("o tipo de primitivo desse valor e: ",type(a))
print("So tem espacos? ",a.isspace())
print("È somente um numero: ", a.isnumeric())
print("E alfabetico: ", a.isalpha())
print("E alfanumerico ? ", a.isalnum())
print("Esta em maiusculas? ", a.isupper())
print("Esta em minusculas ?", a.islower())
print("Esta capitalizada? ", a.istitle()) #quando a palavra não estam todas em maiuscila ou minuscula