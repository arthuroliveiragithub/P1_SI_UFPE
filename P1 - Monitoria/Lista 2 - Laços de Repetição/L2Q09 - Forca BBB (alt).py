fraseCorreta = "PROVA-DO-ANJO-BBB"
letrasDigitadas = ''
vidas = 3

while vidas > 0:
    letra = input().upper()
    fraseTemporaria = ''
    repetida = False
    temLetra = False

    for i in letrasDigitadas:
        if i == letra:
            print(f"Voce ja digitou a letra {letra}")
            repetida = True
    if not repetida:
        letrasDigitadas += letra

    for i in fraseCorreta:
        if i == letra:
            temLetra = True
    if temLetra:
        print("Parabens, voce conseguiu mais uma letra!")
    else:
        vidas -= 1
        if vidas > 0:
            print(f"Que pena, voce tem mais {vidas} chances!")
        elif vidas <= 0:
            print("Fim de jogo, sem almoco do anjo pra voce!")

    for i in fraseCorreta:
        posicao = False
        for j in letrasDigitadas:
            if i == j:
                posicao = True
        if posicao:
            fraseTemporaria += i
        else:
            fraseTemporaria += "-"

    if fraseTemporaria == fraseCorreta:
        print(fraseTemporaria)
        print("Boa, voce e o novo Anjo da semana!")
        vidas = 0
    elif vidas > 0:
        print(fraseTemporaria)
