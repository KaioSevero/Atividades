gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
maior = 0
menor = 10
total_alunos = 0
soma_notas = 0
while True:
    acertos = 0
    for i in range(10):
        resposta = input(f"Resposta da questão {i+1}: ").upper()
        if resposta == gabarito[i]:
            acertos += 1
    print("Nota do aluno:", acertos)
    total_alunos += 1
    soma_notas += acertos
    if acertos > maior:
        maior = acertos
    if acertos < menor:
        menor = acertos
    continuar = input("Outro aluno vai usar o sistema? (S/N): ").upper()
    if continuar == "N":
        break
media = soma_notas / total_alunos
print("Maior acerto:", maior)
print("Menor acerto:", menor)
print("Total de alunos:", total_alunos)
print(f"Média da turma: {media:.2f}")
# Deus te abençoe
