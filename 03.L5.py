total = 0
while True:
    codigo = int(input("Código do produto (0 para sair): "))
    if codigo == 0:
        break
    qtd = int(input("Quantidade: "))
    if codigo == 100:
        preco = 1.20
    elif codigo == 101:
        preco = 1.30
    elif codigo == 102:
        preco = 1.50
    elif codigo == 103:
        preco = 1.20
    elif codigo == 104:
        preco = 1.30
    elif codigo == 105:
        preco = 1.00
    else:
        print("Código inválido!")
        continue
    valor = preco * qtd
    total += valor
    print(f"Item: R$ {valor:.2f}")
print(f"Total do pedido: R$ {total:.2f}")
# Deus te abençoe
