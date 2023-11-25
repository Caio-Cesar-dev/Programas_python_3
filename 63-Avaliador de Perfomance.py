print("=-="*20)
print("***BEM VINDO AO ANALISADOR DE PERFORMANCE***")
print("=-="*20)
print("Informe o valor das vendas, para sair digite o valor 0")
soma=0
cont=0
while True:
    vendas=float(input("Digite o valor das vendas: "))
    if vendas == 0:
        break
    soma += vendas
    cont += 1
    print(f"Subtotal {soma:.2f}")

print('-'*42)
lucro=float(input("Digite o lucro obitido:"))
perfomace=(lucro*100/soma)
print(f"Olá investidor! O total de vendas foi {soma:.2f} Sua Performace foi de {perfomace :.2f} %")

