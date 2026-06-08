cand1 = cand2 = cand3 = cand4 = 0
nulos = brancos = 0
while True:
    voto = int(input("Digite o voto (0 para encerrar): "))
    if voto == 0:
        break
    elif voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Voto inválido!")
total = cand1 + cand2 + cand3 + cand4 + nulos + brancos
if total > 0:
    perc_nulos = nulos * 100 / total
    perc_brancos = brancos * 100 / total
else:
    perc_nulos = 0
    perc_brancos = 0
print("Candidato 1:", cand1)
print("Candidato 2:", cand2)
print("Candidato 3:", cand3)
print("Candidato 4:", cand4)
print("Votos nulos:", nulos)
print("Votos em branco:", brancos)
print(f"% de votos nulos: {perc_nulos:.2f}%")
print(f"% de votos em branco: {perc_brancos:.2f}%")
# Deus te abençoe
