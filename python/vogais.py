palavra = ('aprender','programar','linguagem','python',
'curso','gratis', 'estudar')
for p in palavra:
    print(f' Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')