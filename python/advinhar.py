import random
from time import sleep
print('-=--=--=--=--=--=--=--=--=--=--=--=-=--=--=--=--=--=-')
print('Vou pensar em um numero entre 0 e 5. Tente advinhar')
print('-=--=--=--=--=--=--=--=--=--=--=--=-=--=--=--=--=--=-')
va = random.randint(1,5)
n1 = int(input('Em que numero eu pensei? '))
print('PROCESSANDO.....')
sleep(2)
if n1 == va:
    print(f'Voce acertou eu pensei no numero {va}')
else:
    print('VOCE ERROU HAHAHA')