while True:
    nome = input("Atleta: ")
    if nome == "":
        break
    saltos = []
    for i in range(5):
        salto = float(input(f"{i+1}º Salto: "))
        saltos.append(salto)
    melhor = max(saltos)
    pior = min(saltos)
    saltos.remove(melhor)
    saltos.remove(pior)
    media = sum(saltos) / 3
    print("Melhor salto:", melhor, "m")
    print("Pior salto:", pior, "m")
    print(f"Média dos demais saltos: {media:.1f} m")
    print()
    print("Resultado final:")
    print(f"{nome}: {media:.1f} m")
    print()
# Deus te abençoe
