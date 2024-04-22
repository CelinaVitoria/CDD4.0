rep = "s"
while rep == "S" or rep == "s":
    n = int(input("Digite um número:"))
    if n % 2 == 0:
        print("Par")
    else:
        print("Ìmpar")
    rep = input("Deseja verificar outro número?(s/n)")
