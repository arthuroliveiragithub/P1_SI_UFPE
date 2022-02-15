# 1 - Seguindo o exemplo do dicionário com estoque e operações de venda,
# escreva um programa que solicite ao usuário o produto e a quantidade
# vendida. O programa então deve verificar se o nome do produto digitado
# existe no dicionário, e depois efetuar a baixa no estoque.

estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}

produto = input("Qual o produto vendido? ")
qtd = int(input("Qual a quantidade vendida? "))
venda = [[produto, qtd]]
#print(venda)
#print(produto in estoque)

if (produto in estoque) is True:
    total = 0
    print("Vendas:")
    for operacao in venda:
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
        print(f"Preço: {estoque[chave][1]}")
else:
    print("Produto digitado não faz parte do estoque.")
