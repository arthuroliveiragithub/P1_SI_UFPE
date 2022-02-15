coordA = int(input())
coordB = int(input())
r = int(input())
coordX = int(input())
coordY = int(input())

distancia = ((coordA -coordX)**2 + (coordB - coordY)**2)**0.5

if r > 0:
    if (distancia - 2) <= r:
        print("Esferas do dragao detectadas")
    else:
        print("Esferas fora do radar")
else:
    print("Sua amplitude esta baixa, nao conseguimos te localizar no radar")
