num = int(input("Digite um número: "))
contador = 0

for c in range(1, num + 1):
    if num % c == 0:
        contador += 1

if contador == 2 or contador == 1:#/1 /n
    print("O número é primo")
else:
    print("O número não é primo")