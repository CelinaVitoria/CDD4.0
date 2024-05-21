class Jogo:
    def __init__(self,escolha1 = 0,escolha2 = 0):
        self.escolhaJogador1 = escolha1
        self.escolhaJogador2 = escolha2
    def Jogar(self):
        print(f"o jogador1 escolheu {self.escolhaJogador1}")
        print(f"o jogador2 escolheu {self.escolhaJogador2}")
        if self.escolhaJogador1 == self.escolhaJogador2:
            print("empate")
        elif(self.escolhaJogador1 == 'pedra' and self.escolhaJogador2 == 'tesoura') or \
                (self.escolhaJogador1 == 'papel' and self.escolhaJogador2 == 'pedra') or \
                (self.escolhaJogador1 == 'tesoura' and self.escolhaJogador2 == 'papel'):
            print("O jogador1 venceu")
        elif (self.escolhaJogador2 == 'pedra' and self.escolhaJogador1 == 'tesoura') or \
                (self.escolhaJogador2 == 'papel' and self.escolhaJogador1 == 'pedra') or \
                (self.escolhaJogador2 == 'tesoura' and self.escolhaJogador1 == 'papel'):
            print("O jogador2 venceu")