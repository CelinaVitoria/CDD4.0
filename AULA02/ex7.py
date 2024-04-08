hora1 = int(input("Primeira Hora: "))
minuto1 = int(input("Primeira minuto: "))
hora2 = int(input("Segunda Hora: "))
minuto2 = int(input("Segunda minuto: "))

horas = hora1 + hora2
minutos = minuto1 + minuto2

if minutos >= 60:
    minutos -= 60
    horas += 1

if horas > 12:
   horas -= 12
elif horas < 12:
    horas += 12

if minutos < 10:
    print(f"{int(horas)}:0{minutos}")
else:
    print(f"{int(horas)}:{minutos}")


