n = int(input("Qual o tamanho do vetor? "))
while n < 0:
   print("Erro! O número de estudantes deve ser maior ou igual a 0.")
   n = int(input("Qual o tamanho do vetor? "))
v1 = [0] * n
v2 = [0] * n

for i in range(n):
    v1[i] = int(input(f"Digite o {i+1}º elemento do vetor 1: "))
for i in range(n):
    v2[i] = int(input(f"Digite o {i+1}º elemento do vetor 2: "))

vresultado = v1 + v2

print(v1, v2)
print(vresultado)
