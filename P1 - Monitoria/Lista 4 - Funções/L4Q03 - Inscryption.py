def vencedor_round(a, b):
    if a > b:
        return "ganhou"
    elif a < b:
        return "perdeu"


luke = []
inscryption = []
contador, ganhou, perdeu = 0, 0, 0
for i in range(10):
    nome, vida = input().split("/")
    if i < 5:
        luke.append([nome, int(vida)])
    else:
        inscryption.append([nome, int(vida)])

while ganhou < 3 and perdeu < 3:
    resultado = vencedor_round(luke[contador][1], inscryption[contador][1])
    if resultado == "ganhou":
        output = f"Luke foi muito esperto, usou {luke[contador][0]} e ganhou o {contador + 1}º round!"
        ganhou += 1
    else:
        output = f"Inscryption nao aliviou, usou {inscryption[contador][0]} e venceu o {contador + 1}º round!"
        perdeu += 1
    print(output)
    contador += 1

if ganhou > 2:
    output = "Luke Carter ganhou na batalha de cartas " \
             "e avançou de fase na sua luta para conseguir sair da cabana!"
else:
    output = "Luke Carter foi derrotado na batalha de cartas " \
             "e sua alma permanecera na cabana para todo o sempre!"
print(output)
