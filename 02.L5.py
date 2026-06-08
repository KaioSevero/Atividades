n1 = n2 = n3 = n4 = 0
while True:
    num = float(input("Digite um número: "))
    if num < 0:
        break
    elif num <= 25:
        n1 += 1
    elif num <= 50:
        n2 += 1
    elif num <= 75:
        n3 += 1
    elif num <= 100:
        n4 += 1
print("[0-25]:", n1)
print("[26-50]:", n2)
print("[51-75]:", n3)
print("[76-100]:", n4)
# Deus te abençoe
