neg = 0
for x in range(1,11):
    num = int(input(f"Digite o número {x}:"))
if num < 0:
    neg = neg + 1
print(f"{neg} números são negativos")
