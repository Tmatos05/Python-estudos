from datetime import date
a = date.today().year
ano = int(input('Ano de Nascimento: '))
re = a - ano
if re <= 10:
    print (f'O atleta tem {re} anos')
    print('Classificação: MIRIM')
elif re >= 10 and re <= 21:
    print (f'O atleta tem {re} anos')
    print('Classificação: JUNIOR')
else:
    print (f'O atleta tem {re} anos')
    print('Classificação: SÊNIOR')
