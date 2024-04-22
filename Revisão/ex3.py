idade = int(input("Digite sua idade:"))
mes = int(input("Digite o mês do seu aniversário:"))
if mes >= 4:
    ano = 2024-1 - idade
else:
    ano = 2024 - idade
print(ano)