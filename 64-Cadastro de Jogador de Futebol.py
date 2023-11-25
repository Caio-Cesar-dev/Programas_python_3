"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

jogador={}
jogador['Nome']=str(input('Nome do Jogador: ')).upper()
jogador['Partidas']=int(input(f'Quantas partidas jogador {jogador["Nome"]} jogou: '))
x=tot=0
gols=[]
for x in range(jogador["Partidas"]):
    quant=int(input(f'   Quantos gols marcou na partida {x+1}: '))
    gols.append(quant)
    x+=1
    tot+=quant
jogador['Gols']=gols
jogador['Total']=tot
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'  -O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas:')
for i,v in enumerate(jogador['Gols']):
    print(f' => Na partida {i+1}, fez {v} gols')

