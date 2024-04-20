ss = 1234
x = 0
senha = int(input("digite a senha:"))
while senha != ss:
    senha = int(input("digite a senha:"))
    x = x + 1
    if x == 2 and ss != senha:
        print("senha bloqueada")
        break
else:
    print("login realizado")
