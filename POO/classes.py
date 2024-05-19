class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno,comendo=False,falando=False,dormindo=False):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo
    def comer(self,alimento):
        if self.comendo == False and self.falando == False and self.dormindo == False:
            self.comendo = True
            print(f"{self.nome} está comendo {alimento}")
        elif self.comendo == True:
            print(f"{self.nome} já está comendo")
        elif self.falando == True:
            print(f"{self.nome}  está falando")
        elif self.dormindo == True:
            print(f"{self.nome}  está dormindo")
    def parardecomer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer")
        elif self.comendo == False:
            print(f"{self.nome} não está comendo")
        elif self.falando == True:
            print(f"{self.nome} está falando")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo")
    def falar(self):
        if self.comendo == False and self.falando == False and self.dormindo == False:
            self.falando = True
            print(f"{self.nome} está falando")
        elif self.comendo == True:
            print(f"{self.nome} está comendo")
        elif self.falando == True:
            print(f"{self.nome} está falando")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo")
    def parardefalar(self):
        if self.falando == True:
            self.falando = False
            print(f"{self.nome} parou de falar")
        elif self.falando == False:
            print(f"{self.nome} não está falando")
        elif self.comendo == True:
            print(f"{self.nome} não está comendo")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo")
    def dormir(self):
        if self.comendo == False and self.falando == False and self.dormindo == False:
            self.dormindo = True
            print(f"{self.nome} está dormindo")
        elif self.comendo == True:
            print(f"{self.nome} está comendo")
        elif self.falando == True:
            print(f"{self.nome} está falando")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo")

    def parardedormir(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f"{self.nome} parou de dormir")
        elif self.dormindo == False:
            print(f"{self.nome} não está dormindo")
        elif self.falando == True:
            print(f"{self.nome} está falando")
        elif self.comendo == True:
            print(f"{self.nome} está comendo")
