class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno,comendo=False,falando=False,dormindo=False):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo
    def comer(self,alimento):
        print(f"{self.nome} foi comer {alimento}")
        self.comendo=True
    def parardecomer(self):
        print(f"{self.nome} parou de comer")
        self.comendo = False
    def falar(self,fala):
        print(f"{self.nome} falou {fala}")
        self.falando = True
    def parardefalar(self):
        print(f"{self.nome} parou de falar")
        self.comendo = False
    def dormir(self,dorme):
        print(f"{self.nome} {dorme}")
        self.dormindo = True
    def parardedormir(self):
        print(f"{self.nome} parou de dormir")
        self.comendo = False