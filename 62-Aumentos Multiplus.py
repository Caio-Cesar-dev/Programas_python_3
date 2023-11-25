"""Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

nome=str(input("Digite o NOME do funcionário: ")).strip()
sal=float(input("Informe o SALÁRIO do funcionário: "))

if sal > 1250:
    print("O salário do colaborador {},com ajuste de 10%, será de {:.2f} reais".format(nome, sal+(sal*0.10)))
else:
    if sal <= 1250:
        print("O salário do colaborador {}, com o ajuste de 15 % será de {:.2f} reais".format(nome, sal+(sal*0.15)))