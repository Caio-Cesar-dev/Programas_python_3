import requests,json
request=requests.get('https://economia.awesomeapi.com.br/all/USD-BRL').json()
vlr_atual= request['USD']['bid']
vlr_atual=float(vlr_atual)
nica=float(input("Quanto voce tem de grana(reais) que converto em dolares: R$ "))
div=nica/vlr_atual
print(f'Valor hoje do dolar {vlr_atual:.2f}')
print(f'Você tem o equivalente a $ {div:.2f} em dolares.')




#print("A cotação do dolar é de R$ 5,31 em 06/01/2021")