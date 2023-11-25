valor_acao= float(input("Didite o valor da ação: "))
valor_opcao= float(input("Digite o valor da opção: "))
strike = float(input("Digite o valor do strike: "))
qt_acoes = int(input("Digite a quantidade de ações: "))
qt_opcoes = int(input("Digite a quantidade de opções:"))
premio= valor_opcao * qt_opcoes
valor_investido= (valor_acao - valor_opcao) * qt_acoes # duvidas se está certo esse cálculo

custo_exerc= qt_acoes * strike * 0.005 + ((qt_acoes * strike * 0.005) * 0.1068)

luc_bruto = (strike - valor_acao + valor_opcao) * qt_acoes
luc_liquido = luc_bruto - custo_exerc - ((luc_bruto - custo_exerc) * 0.15)
result_percent= (luc_liquido * 100) / valor_investido




#custos_totais= (((strike - valor_acao) * qt_acoes) + premio - custo_exerc) * 0.15
valor_intrinseco= valor_acao - strike
valor_extrinseco= valor_opcao - valor_intrinseco

valor_percentual= (valor_extrinseco * 100) / valor_acao # valor percentual bruto


print(14 * '-=-')
print(f"O custo de exercício na Clear: R$ {custo_exerc:.2f}")
print(f"O lucro bruto: R$ {luc_bruto:.2f} ")
print(f"O lucro liquido: R$ {luc_liquido :.2f}") #lucro liquido descontado o IR
print(f"O resultado percentual líquido {result_percent :.2f} %")

print(14 * '-=-')
print("-=-=-=-=-=TABELA DE PROJEÇÃO-=-=-=-=-=- ")
#print(14 * '-=-')
print(f"Estimativa de proteção de 3 % : R$ {valor_acao -(valor_acao * 0.03 ) }")
print(f"Estimativa de proteção de 4 % : R$ {valor_acao -(valor_acao * 0.04) }")
print(f"Estimativa de proteção de 5 % : R$ {valor_acao -(valor_acao * 0.05) }")
print(f"Estimativa de proteção de 6 % : R$ {valor_acao -(valor_acao * 0.06) }")
print(f"Estimativa de proteção de 7 % : R$ {valor_acao -(valor_acao * 0.07) }")
print(f"Estimativa de proteção de 8 % : R$ {valor_acao -(valor_acao * 0.08) }")
print(f"Estimativa de proteção de 9 % : R$ {valor_acao -(valor_acao * 0.09) }")
print(f"Estimativa de proteção de 10 % : R$ {valor_acao -(valor_acao * 0.10) }")
print(f"Estimativa de proteção de 11 % : R$ {valor_acao -(valor_acao * 0.11) }")
print(f"Estimativa de proteção de 12 % : R$ {valor_acao -(valor_acao * 0.12) }")
print(f"Estimativa de proteção de 13 % : R$ {valor_acao -(valor_acao * 0.13) }")
print(f"Estimativa de proteção de 14 % : R$ {valor_acao -(valor_acao * 0.14) }")
print(f"Estimativa de proteção de 15 % : R$ {valor_acao -(valor_acao * 0.15) }")
print(12 * '-=-')

print(f"O valor intrinsico: R$ {valor_intrinseco:.2f} e o valor extrinsico: R$ {valor_extrinseco:.2f}")
print(f"Valor percentual bruto: {valor_percentual:.2f} porcentos")



