tipo= input("digite o tipo de combustível\n(E para etanol e g para gasolina):")
litros= float(input( "digite o n de litros:"))
etanol= 4.90
gasolina= 5.80
if tipo== "G"or tipo=="g":
    total= gasolina*litros
    print(f"voce gastou{total}")
elif tipo == "e" or tipo == "E":
    total= etanol*litros
    print(f"voce gastou {total}")
else:
    print("tipo de combustível inválido")