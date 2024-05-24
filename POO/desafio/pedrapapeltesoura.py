class Jogo():
    def __init__(self,escolha1 = 0,escolha2 = 0):
        self.escolha1 = escolha1
        self.escolha2 = escolha2
        self.placarJogador1 = 0
        self.placarJogador2 = 0
    def Jogar(self,escolha1,escolha2):
            if(escolha1 == 'pedra' and escolha2 == 'tesoura') or \
                    (escolha1 == 'papel' and escolha2 == 'pedra') or \
                    (escolha1 == 'tesoura' and escolha2 == 'papel'):
                print("O jogador 1 venceu uma rodada")
                self.placarJogador1 +=1
            elif (escolha2 == 'pedra' and escolha1 == 'tesoura') or \
                    (escolha2 == 'papel' and escolha1 == 'pedra') or \
                    (escolha2 == 'tesoura' and escolha1 == 'papel'):
                print("O jogador 2 venceu uma rodada")
                self.placarJogador2 += 1
            else:
                print("Uma rodada deu empate")
    def Contar(self):
            if self.placarJogador1 > self.placarJogador2:
                print("O jogador 1 venceu a partida")
            elif self.placarJogador2 > self.placarJogador1:
                print("O jogador 2 venceu a partida")
            elif self.placarJogador1 == self.placarJogador2:
                print("a partida acabou em empate")
