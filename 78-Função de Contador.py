"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada """
from time import sleep
def contador(*num):
    print('-='*15)
    print('Contagem de 1 até 10 de 1 em 1. ')
    for i in range(1,11,1):
        print(i,end=' ')
        sleep(0.3)
    print('FIM!!!')
    print('-=' * 15)
    print('Contagem de 10 até 0 de 2 em 2. ')
    for i in range(10, -1, -2):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!!!')
    print('-=' * 15)
    print('Agora sua vez de pesonalizar a contagem! ')
    ini = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-='*15)
    print(f'Contagem de {ini} até {fim+1} de {passo} em {passo}')
    for i in range(ini, fim, passo):
        print(i, end=' ')
        sleep(0.3)
    print('FTM!!!')



contador()


