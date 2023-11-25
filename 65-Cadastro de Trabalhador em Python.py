"""Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date

cadastro={}
cadastro['Nome']=str(input('Nome: ')).upper()
ano_nasc=int(input('Ano de nascimento: '))
cadastro['Idade: ']=(date.today().year - ano_nasc)
cadastro['Carteira de trabalho']=int(input('Carteira de trabalho(0 Não tem!): '))
if cadastro['Carteira de trabalho'] != 0:
    cadastro['Ano de contratação']=int(input('Ano de contratação: '))
    cadastro['Salário']=float(input('Salário: R$  '))
    cadastro['Aposentadoria']=((cadastro['Ano de contratação']-ano_nasc)+35)

print('-='*30)

for k,v in cadastro.items():
    print(f' -{k} tem o valor [{v}]')
