nome_1 = input()
vida_1 = int(input())
ataque_1 = int(input())
defesa_1 = int(input())
nome_2 = input()
vida_2 = int(input())
ataque_2 = int(input())
defesa_2 = int(input())

# Round 1 - obrigatório
print("Round 1")
golpe = input()
defesa = input()
dano = 0
if golpe == "jab":
    if defesa == "bloqueio":
        dano = (ataque_1 - (ataque_1 * defesa_2/100))
    elif defesa == "esquiva":
        ataque_2 = ataque_2 * 1.1
    elif defesa == "X":
        dano = ataque_1
elif golpe == "direto":
    if defesa == "bloqueio":
        dano = (ataque_1 * 1.3 - (ataque_1 * defesa_2/100))
    elif defesa == "esquiva":
        ataque_2 = ataque_2 * 1.2
    elif defesa == "X":
        dano = ataque_1 * 1.4
vida_2 = vida_2 - int(dano)

if vida_2 > 0:
    # Vamos para o Round 2
    print("Round 2")
    golpe = input()
    defesa = input()
    dano = 0
    if golpe == "jab":
        if defesa == "bloqueio":
            dano = (ataque_2 - (ataque_2 * defesa_1 / 100))
        elif defesa == "esquiva":
            ataque_1 = ataque_1 * 1.1
        elif defesa == "X":
            dano = ataque_2
    elif golpe == "direto":
        if defesa == "bloqueio":
            dano = (ataque_2 * 1.3 - (ataque_2 * defesa_1 / 100))
        if defesa == "esquiva":
            ataque_1 = ataque_1 * 1.2
        if defesa == "X":
            dano = ataque_2 * 1.4
    vida_1 = vida_1 - int(dano)

    if vida_1 > 0:
        # Vamos para o Round 3
        print("Round 3")
        print(f"{nome_1.upper()} SO TEM MAIS UM ROUND PARA DERRUBAR SEU ADVERSARIO")
        golpe = input()
        defesa = input()
        dano = 0
        if golpe == "jab":
            if defesa == "bloqueio":
                dano = (ataque_1 - (ataque_1 * defesa_2 / 100))
            if defesa == "esquiva":
                ataque_2 = ataque_2 * 1.1
            if defesa == "X":
                dano = ataque_1
        if golpe == "direto":
            if defesa == "bloqueio":
                dano = (ataque_1 * 1.3 - (ataque_1 * defesa_2 / 100))
            if defesa == "esquiva":
                ataque_2 = ataque_2 * 1.2
            if defesa == "X":
                dano = ataque_1 * 1.4
        vida_2 = vida_2 - int(dano)
        if vida_1 > vida_2:
            print(f"NOSSO CAMPEAO E {nome_1.upper()}")
        elif vida_2 > vida_1:
            print(f"NOSSO CAMPEAO E {nome_2.upper()}")
    else:
        print(f"NOSSO CAMPEAO E {nome_2.upper()}")
else:
    print(f"NOSSO CAMPEAO E {nome_1.upper()} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND")
