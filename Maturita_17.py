# tajna tabulka
veta = input("Zadaj vetu: ")

pocty = [0] * 10
sifra = ""

for i in veta:
    if i == " ":
        kod = "0"
    else:
        policko = str((ord(i) - 65) // 3 + 1)
        kod = policko * ((ord(i) - 65) % 3 + 1)
    sifra += kod + " "
    for x in kod:
        pocty[int(x)] += 1

print("Zašifrovaná veta:")
print(sifra)

najviac = max(pocty)
print("Najčastejšie zvolené políčka:", end=" ")
for i in range(10):
    if pocty[i] == najviac:
        print(i, end=" ")
