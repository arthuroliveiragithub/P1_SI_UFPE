estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}

venda = [["tomate", 8], ["batata", 12], ["alface", 8]]

total = 0
print("Vendas:")
for operacao in venda:
    produto = operacao[0]
    qtd = operacao[1]
    preco = estoque[produto][1]
    custo = preco * qtd
    print(f"{produto}: {qtd} x {preco:.2f} = {custo:.2f}")
    estoque[produto][0] -= qtd
    total += custo
print(f"Custo total: {total:.2f}\n")
print("Estoque:\n")
for chave in estoque:
    print(f"Descrição: {chave}")
    print(f"Quantidade: {estoque[chave][0]}")
    print(f"Preço: {estoque[chave][1]:.2f}\n")
