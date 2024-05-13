def cadastro():
    nomes = ["","","","",""]
    senhas = ["","","","",""]
    for x in range(5):
        nomes = input("digite nome:")
        senhas = int(input("digite a senha:"))
def imprime_nome(nome):
    print(f"nome: {nome}")
def piramide(n):
    for x in range(1,n+1):
        for y in range(1, x+1):
            print(x,end = " ")
        print()
def piramide2(j):
    for x in range(1,j+1):
        for y in range(1,x+1):
            print(y,end = " ")
        print()
def vogais(texto):
    cont1 = 0
    cont2 = 0
    for z in texto:
        if z == " ":
            cont1 = cont1 + 1
    for x in texto:
        if x in "aeiouAEIOU":
            cont2 = cont2 + 1
    print(cont1)
    print(cont2)
def estoque(nome, quant, valor):
    total = quant * valor
    return total