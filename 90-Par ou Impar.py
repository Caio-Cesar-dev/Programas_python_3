"""Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""
num=int(input("Digite um numero qualquer: "))
if num % 2 ==0:
    print(f"{num} é um número PAR!" )
else:
    print(f"{num} é um numero IMPAR!")