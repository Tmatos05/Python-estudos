valor = int(input('Valor do imovel: R$ '))
salario = int(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
pestraçao = valor / (anos * 12)
minimo = salario * 30 /100
print(f'Para pagar uma casa de R${valor}.00 em {anos} a prestação sera de {pestraçao}')
print(f'COMPARANDO tem que pagar {pestraçao} e o minimo é de {minimo}')
if pestraçao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo Negado!!')