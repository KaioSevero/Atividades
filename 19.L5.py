texto = input("Digite uma frase: ").lower()
vogais = 0
consoantes = 0
for letra in texto:
    if letra in "aeiou":
        vogais += 1
    elif letra.isalpha():
        consoantes += 1
print("Vogais:", vogais)
print("Consoantes:", consoantes)
# Deus te abençoe
