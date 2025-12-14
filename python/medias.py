n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
valor = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {valor}')
if valor >= 7:
    print('O aluno foi aprovado')
elif valor >= 5:
    print('O aluno esta de RECUPERAÇÃO')
else:
    print('O aluno foi REPROVADO')