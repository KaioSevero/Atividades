n = int(input("Ordem da matriz: "))
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
soma_principal = 0
soma_secundaria = 0
for i in range(n):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][n - 1 - i]
print("Soma da diagonal principal:", soma_principal)
print("Soma da diagonal secundária:", soma_secundaria)
# Deus te abençoe
