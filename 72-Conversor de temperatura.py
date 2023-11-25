escolha=int(input("Digite '1' para obter Fahrenheit ou digite '2' para obter Graus Celsios:  " ))


if (escolha == 1):
    temp1 = float(input("Digite a temperatura em graus celsios: "))
    print("A temperatura em Fahrenheit é de : {} F" .format((temp1*9)/5 + 32))
else:
    if(escolha == 2):
        temp2 = float(input("Digite a temperatura em Fahrenheit: "))
        print("A temperatura em graus Celsios é de : {:.1f} C".format((temp2-32)*5/9))