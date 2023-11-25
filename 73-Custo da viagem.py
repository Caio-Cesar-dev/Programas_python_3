"""Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

print("*" * 40)
dist=float(input("Informe a diastância percorrida em Km: "))
print('-'*40)
if dist <= 200:
    print("O valor a ser cobrado será de R$ {:.2f} Reais".format(dist*0.50))
else:
    if dist > 200:
        print("O valor a ser cobrado será de R$ {:.2f} Reais".format(dist*0.45))

print('*' * 40)
print("Foi um prazer tê-lo conosco!!!")