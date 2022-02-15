a = int(input())
l = int(input())
p = int(input())
h = int(input())

max1 = (a + l + abs(a - l))/2 #tirando o máximo entre A e L
max2 = (max1 + p + abs(max1 - p))/2 #tirando o máximo entre o priemro máximo e P
m = int(max2 * h) #multiplicando pela quantidade de horas

print(m)
