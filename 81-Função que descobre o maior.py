"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep
def maior(*num):
    cont=maior=0
    print('-='*23)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f' {valor} ',end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


#Programa principal
maior(2,4,5,9,8,7)
maior(2,5,7)
maior(1,7)
maior(6)
maior()


"""
def maior(*num):
    cont=maior=0
    print('-='*23)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f' {valor} ',end=' ')
    print(f'\n E o maior número informado foi  {max(num)}')

#Programa principal
maior(2,4,5,9,8,7)
maior(2,5,7)
maior(1,7)
maior(6)
#maior() #O programa não finaliza devido eese parametro vazio, a função 'max' não reconhece."""