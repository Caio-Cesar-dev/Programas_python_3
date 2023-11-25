"""Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""

from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: Voto NEGADO.'
    elif 16 <= idade <18 or idade > 70:
        return f'Com {idade} anos: Voto OPCIONAL'
    else:
        return f'Com {idade} anos: Voto OBRIGATÓRIO'


print('-'*35)
ano=int(input('Informe o seu ano de nascimento: '))
print(voto(ano))