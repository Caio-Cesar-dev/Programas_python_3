"""Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno."""

def area(largura, comprimento):
    area=largura*comprimento
    print('-='*20)
    print(f"A área de um terreno {largura} x {comprimento} é de {area}m².")
    print('-='*20)


print("Controle de Terrenos")
print("--------------------")
largura=float(input("Informe a largura do terreno (m): "))
comprimento=float(input("Informe o comprimento do terreno(m): "))
area(largura,comprimento)