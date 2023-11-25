prod=float(input("Digite o valor do produto: "))
desc=int(input("digite a porcentagem do desconto: "))
desc=(prod*(desc/100))
vlr_final=prod-desc
print("O produto custava {:.2f} reais, agora com o desconto de {:.2f} reais sai por {:.2f} reais" .format(prod,desc,vlr_final))