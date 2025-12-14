print("Digite números para descobrir o maior e menor. Digite 0 para parar.")

max_num = None
min_num = None

while True:
    num = int(input("Digite um número: "))
    
    if num == 0:
        break  # sai do loop
    
    # atualiza o maior número
    if max_num is None or num > max_num:
        max_num = num
    
    # atualiza o menor número
    if min_num is None or num < min_num:
        min_num = num

print(f"Você encerrou o loop.")
print(f"O maior número digitado foi {max_num}")
print(f"O menor número digitado foi {min_num}")
