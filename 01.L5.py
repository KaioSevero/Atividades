divida = float(input("Dívida: "))
parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]
for i in range(5):
    total = divida + divida * juros[i] / 100
    parcela = total / parcelas[i]
    print(total, divida * juros[i] / 100, parcelas[i], round(parcela, 2))
 # Deus te abençoe
