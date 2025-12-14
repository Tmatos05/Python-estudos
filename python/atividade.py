import random
n1 = random.randint(1,11)
n2 = random.randint(1,11)
s = n1 + n2
print(f'{n1} + {n2} = ')

while True:
    r = int(input('Qual o valor da soma? '))
    if r == s:
        print ('Voce acertou!!!')
        break
    elif r != s:
        print('voce ERROU, TENTE NOVAMENTE')    
    