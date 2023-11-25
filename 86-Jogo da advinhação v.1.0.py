"""xercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu."""

from random import randint
from time import sleep

computador = randint(0,5) #faz o computador escolher entre o inicio e fim dos numeros
print('-=-' * 20)
nome=str(input("Qual o seu nome: "))
print(f"Olá {nome}!! \nEu sou o Mr Robbot. ")
print("Vou pensar em um número entre 0 e 5. Tente adivinhar!!")
print("-=-" * 20)

jogador= int(input("Em que numero eu pensei? "))#jogador tenta advinhar
print("PROCESSADO...")
sleep(2)#processa por um tempo... da a impressao de que a maquina está pensando na resposta

if jogador == computador:
    print(f"PARABÊNS{nome}! Você conseguiu me vencer!")
else:
    print("_MR Robot: GANHEI! Eu pensei no numero {} e não no numero {} ".format(computador,jogador))


