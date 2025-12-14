n = int(input('Digite um número entre 0 e 20: '))
while n > 20:
    print('Número fora do intervalo. Tente novamente!')
    n = int(input('Digite um número entre 0 e 20: '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número {extenso[n]}.')