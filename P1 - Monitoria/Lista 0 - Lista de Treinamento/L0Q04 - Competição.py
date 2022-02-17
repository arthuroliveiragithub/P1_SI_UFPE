a = int(input())
l = int(input())
p = int(input())
h = int(input())

max = (a + l + abs(a - l))/2 #tirando o máximo entre A e L
max = (max + p + abs(max - p))/2 #tirando o máximo entre o priemro máximo e P
max = int(max * h) #multiplicando pela quantidade de horas

print(max)
