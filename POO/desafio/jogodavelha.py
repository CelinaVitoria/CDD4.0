def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            print(elemento, end=" ")
        print()

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" "]*3 for _ in range(3)]
    jogador_atual = "X"

    while True:
        print_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                print_tabuleiro(tabuleiro)
                print(f"Parabéns, jogador {jogador_atual} venceu!")
                break
            elif all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
                print_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Escolha outra.")

jogar_jogo_da_velha()

