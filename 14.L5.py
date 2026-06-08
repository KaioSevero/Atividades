linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
transposta = []
for j in range(colunas):
    linha = []
    for i in range(linhas):
        linha.append(matriz[i][j])
    transposta.append(linha)
print("Matriz Transposta:")
for linha in transposta:
    print(linha)
# Deus te abençoe
