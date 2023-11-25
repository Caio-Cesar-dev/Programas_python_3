"""Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""
n= int(input("Digite um numero: "))
print()
print("O dobro de {} é igual a: {} " .format(n, (n*2)))
print("O tripulo de {} é igual a: {} \ne a raiz quadrada de {} é igual a: {:.2f} ".format(n,(n*3),n,(n**(1/2))))