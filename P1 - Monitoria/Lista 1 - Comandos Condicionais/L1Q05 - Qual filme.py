nome1, nota1, duracao1 = input().split("-")
nome2, nota2, duracao2 = input().split("-")
nome3, nota3, duracao3 = input().split("-")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
duracao1 = int(duracao1)
duracao2 = int(duracao2)
duracao3 = int(duracao3)
maiornota = 0

if nota1 >= 4 or nota2 >= 4 or nota3 >= 4:
    if nota1 >= nota2 and nota1 >= nota3:
        if nota1 > nota2 and nota1 > nota3:
            print(nome1)
        if nota1 == nota2 and nota1 > nota3:
            if duracao1 < duracao2:
                print(nome1)
            else:
                print(nome2)
        elif nota1 == nota3 and nota1 > nota2:
            if duracao1 < duracao3:
                print(nome1)
            else:
                print(nome3)
        elif nota1 == nota2 and nota1 == nota3:
            if duracao1 < duracao2 and duracao1 < duracao3:
                print(nome1)
            elif duracao2 < duracao1 and duracao2 < duracao3:
                print(nome2)
            elif duracao3 < duracao1 and duracao3 < duracao2:
                print(nome3)
    elif nota2 > nota1 and nota2 >= nota3:
        if nota2 > nota3:
            print(nome2)
        elif nota2 == nota3:
            if duracao2 < duracao3:
                print(nome2)
            elif duracao3 < duracao2:
                print(nome3)
    elif nota3 > nota1 and nota3 > nota2:
        print(nome3)
else:
    print("Nota minima nao atingida")
