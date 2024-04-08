hora1 = int(input("Primeira hora: "))
minuto1 = int(input("Primeira minuto: "))
hora2 = int(input("Segunda hora: "))
minuto2 = int(input("Segunda minuto: "))
if hora1 > 12:
    hora1 = hora1 - 12
if hora2 > 12:
    hora2 = hora2 - 12
horas = hora1 + hora2
minutos = minuto1 + minuto2
if minutos >= 60:
    minutos = minutos - 60
    horas = horas + 1
if minutos < 10:
    print(f"{int(horas)}:0{minutos}")
else:
    print(f"{int(horas)}:{minutos}")
