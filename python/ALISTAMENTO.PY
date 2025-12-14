from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
anos = atual - nasc 
print(f'Quem nasceu em {atual} tem {anos} anos em 2025')
if anos == 18:
    print('Voce tem que se alisatr IMEDIATAMENTE!')
elif anos <18:
    saldo = 18 - anos
    print(f'Voce ainda nao tem 18 anos. Ainda faltam {saldo} anos para o alistamento')
elif anos >18:
    saldo = anos - 18
    print(f'Voce ja deveria ter se alistado ha {saldo} anos')