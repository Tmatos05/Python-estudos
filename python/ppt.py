import random

opcoes = ["pedra", "papel", "tesoura"]

print("=== Pedra, Papel e Tesoura ===")

jogador_pontos = 0
pc_pontos = 0

while True:
    print("\nDigite sua opção: pedra, papel ou tesoura")
    print("Ou 'sair' para encerrar o jogo.")
    jogador = input("Você: ").strip().lower()

    if jogador == "sair":
        print("\nJogo encerrado!")
        break

    if jogador not in opcoes:
        print("Opção inválida! Tente novamente.")
        continue

    pc = random.choice(opcoes)
    print(f"Computador: {pc}")

    # Empate
    if jogador == pc:
        print("Empate!")

    # Vitórias do jogador
    elif (
        (jogador == "pedra" and pc == "tesoura") or
        (jogador == "papel" and pc == "pedra") or
        (jogador == "tesoura" and pc == "papel")
    ):
        print("Você ganhou! 🎉")
        jogador_pontos += 1
    else:
        print("Você perdeu! 😅")
        pc_pontos += 1

    print(f"Placar -> Você: {jogador_pontos} | Computador: {pc_pontos}")

print(f"\nPlacar final -> Você: {jogador_pontos} | Computador: {pc_pontos}")
print("Obrigado por jogar!")
