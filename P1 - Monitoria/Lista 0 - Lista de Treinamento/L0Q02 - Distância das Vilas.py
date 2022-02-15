x_atual = int(input())
z_atual = int(input())

h = ((34 - x_atual)**2 + (220 - z_atual)**2)**0.5
k = ((0 - x_atual)**2 + (0 - z_atual)**2)**0.5
s = ((140 - x_atual)**2 + (456 - z_atual)**2)**0.5

print(f"Distancia para Hogsmeade: {h:.2f}")
print(f"Distancia para Kakariko: {k:.2f}")
print(f"Distancia para Solitude: {s:.2f}")
