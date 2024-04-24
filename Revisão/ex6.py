pedido = 0
while pedido != 3:
    pedido = int(input("Digite 1 para a área do triângulo ou 2 para a area do quadrado e três para sair:"))
    if pedido > 3 or pedido <1:
        print("Número inválido")
    if pedido == 1:
        lado = float(input("Digite o valor do lado do quadrado:"))
        area = lado**2
        print(area)
    elif pedido == 2:
        base = float(input("Digite o valor da base do triângulo:"))
        altura = float(input("Digite o valor da altura do triângulo:"))
        area = (base * altura)/2
        print(area)
