num = int(input("Digite um número:"))
if num == 0:
    num = int(input("Digite outro número:"))
    for x in range(1, num+1):
        print(x, end=" ")
else:
    for x in range(1, num+1):
        print(x, end=" ")