print('========LOJA THIAGO==========')
preço = int(input('Preço das compras: R$'))
print(''''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
es = int(input('Qual é a opção?'))
if es == 1:
    des = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço}.00 vai custar R${des}.00 no final')
elif es == 2:
    des = preço - (preço * 5 / 100)
    print(f'Sua compra de R${preço}.00 vai custar R${des}.00 no final')
elif es == 3:
    print(f'Sua compra dividindoo valor em 2x fica R${preço}.00')
elif es == 4:
     juros = preço - (preço * 20 / 100)
     par = int(input('Quantas parcelas? '))
     total = juros / par
     print(f'Sua compra sera parcelada em {par}x de R${total}')
     print(f'Sua compra de R${preço} vai custar R${juros}')