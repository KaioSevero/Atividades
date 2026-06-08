linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
elemento = int(input("Elemento a procurar: "))
contador = 0
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == elemento:
            contador += 1
print("Quantidade de vezes que aparece:", contador)
# Deus te abençoe
