#

letra = input().upper()
numero = int(input())

if numero % 2 == 1 and numero > 1 and (letra == "X" or letra == "T" or letra == "O"):
    if letra == "T":
        for i in range(numero):
            for j in range(numero):
                if i == 0 or j == numero // 2:
                    print("X", end="")
                else:
                    print("0", end="")
            print("\n")
    elif letra == "O":
        for i in range(numero):
            for j in range(numero):
                if i == 0 or i == numero - 1 or j == 0 or j == numero - 1:
                    print("X", end="")
            else:
                print("0", end="")
            print("\n")
    elif letra == "X":
        for i in range(numero):
            for j in range(numero):
                if j == i or j == (numero - (i + 1)):
                    print("X", end="")
                else:
                    print("0", end="")
            print("\n")
else:
    print("Entrada não permitida")
