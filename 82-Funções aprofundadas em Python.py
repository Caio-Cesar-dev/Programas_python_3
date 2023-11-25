"""Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

def leiaInt(msg):
    while True:
        try:
            n= int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mError: por favor, digite um número válido!\033[m')
            continue
        except (KeyboardInterrupt):   #este comando não funciona como na aula
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro,: por favor, digite um número válido!\033[m ')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário ')
            return 0
        else:
            return n


num = leiaInt('Digite um valor inteiro: ')
num2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {num}')
print(f'O valor Real digitado foi {num2} ')