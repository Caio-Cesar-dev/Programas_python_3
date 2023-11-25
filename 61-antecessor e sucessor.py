"""Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor
e seu antecessor."""
n=int(input("Digite um numero: "))
a= n-1
s= n+1
print("Analisado o valor {}, seu antecessor é {} e o seu sucessor é {}".format(n,a,s))
# ou temos esta opcao{ .format(n, (n-1), (n+1) } .