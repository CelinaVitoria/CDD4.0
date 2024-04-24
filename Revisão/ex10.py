dia = int(input("digite o dia em que você nasceu:"))
mes = int(input("digite o mês em que você nasceu:"))
ano = int(input("digite o ano em que você nasceu:"))
anos = 2024 - ano
meses = mes - 4
dias = dia - 24
if mes > 4:
    diferença = 2024-1 - ano
    print(f"Você tem {anoidade} anos, {meses} meses  e {dias} dias de vida ")
if dia < 24:
    diferença = 24 - dia
    print(f"Você tem {anoidade} anos, {mesidade} meses  e {dias} dias de vida ")
else:
    print(f"Você tem {anos} anos, {meses} meses  e {dias} dias de vida ")
