valor = int(input('Quak a distancai da viagem? '))
if valor <= 200:
    preco = valor * 0.50
    print (f'A viagem custará {preco}0 R$')
else: 
    preco = valor * 0.45
    print(f'A viagem custará {preco}0 R$')