linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
nova = []
for i in range(linhas - 1, -1, -1):
    nova.append(matriz[i])
print("Nova matriz:")
for linha in nova:
    print(linha)
# Deus te abençoe
