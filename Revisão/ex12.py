inicio = int(input("digite a hora de inicio do jogo de xadrez:"))
fim = int(input("digite a hora de fim do jogo de xadrez:"))
if inicio > fim:
    duracao = 24 - inicio + fim
elif inicio < fim:
    duracao = fim - inicio
print(f"{duracao} horas")