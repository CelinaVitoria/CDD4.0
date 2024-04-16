dentro = 0
fora = 0
for x in range(1,11):
    num = int(input(f"Digite o número {x}:"))
    if num >= 10 and num <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print(f"{dentro} números estão dentro do intervalo")
print(f" {fora} estão fora do intervalo")
