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
class conta():
    def __init__(self, nmrconta, nomecliente, tipoconta,):
        self.nmr = nmrconta
        self.sld = valor = 0
        self.stts = False
        self.nm = nomecliente
        self.tpconta = tipoconta
    def ativar(self,status = False):
        if status == "ativar":
            self.stts = True
            print("a conta está ativada")
    def desativar(self,status = False):
        if status == "deativar":
            self.stts = False
            print("a conta está ativada")
    def depositar(self,valor):
        self.sld += valor
        if self.stts == False:
            print("A conta está desativada, ative")
        else:
            print(f"{self.nm} inseriu R${valor} na conta")
    def sacar(self, valor):
        if self.stts == False:
            print("A conta está desativada, ative")
        else:
            if valor < self.sld:
                print(f"{self.nm} sacou R${valor}")
                self.sld -= valor
            else:
                print("você não possue esse valor para sacar")
    def verificar(self):
        if self.stts == False:
            print("A conta está desativada, ative")
        else:
            print(f"o saldo presente na conta é de R${self.sld}")
class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0
class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculaArea( b, h):
        self.area = b * h
    def calculaPerimetro( b, h):
        self.perimetro = 2(b * h)
        print(f"A are do retangulo é {self.area} e o perimetro do retangulo é {self.perimetro}")
class Triangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculaArea( b, h):
        self.area = (b * h) / 2
    def calculaPerimetro(l):
        self.perimetro = 3 * l
        print(f"A are do retangulo é {self.area} e o perimetro do retangulo é {self.perimetro}")

