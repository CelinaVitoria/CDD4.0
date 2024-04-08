t1=input("digite time 1:")
t2=input("digite time 2:")

gol_t1=int(input("n de gols do t1:"))
gol_t2=int(input("n de gols do t2:"))

if gol_t1==gol_t2:
    print("empate")
elif gol_t1>gol_t2:
    print("O {t1} venceu")
else:
    print("O {t2} venceu")
