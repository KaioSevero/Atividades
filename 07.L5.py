while True:
    nome = input("Atleta: ")
    if nome == "":
        break
    notas = []
    for i in range(7):
        nota = float(input("Nota: "))
        notas.append(nota)
    melhor = max(notas)
    pior = min(notas)
    notas.remove(melhor)
    notas.remove(pior)
    media = sum(notas) / 5
    print("\nResultado final:")
    print("Atleta:", nome)
    print("Melhor nota:", melhor)
    print("Pior nota:", pior)
    print(f"Média: {media:.2f}\n")
# Deus te abençoe
