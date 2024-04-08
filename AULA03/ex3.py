num = int(input("digite o número:"))
print(f"A tabuada de {num} é:")
for x in range(1,11):
    soma = num * x
    print (f"{num} x {x} ={soma} ")