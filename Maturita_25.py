import random
# vstup
tip = input("Zadaj tip na 6 čísel v lotérii: ")
cisla = []
for c in tip.split():
    cisla.append(int(c))
print("Tvoj tip:", cisla)
# žrebovanie simulacia
zrebovane = random.sample(range(1, 50), 6)
print("Vyžrebované:", zrebovane)
# rovnake
uhadnute = []
for c in cisla:
    if c in zrebovane:
        uhadnute.append(c)
print("Uhádnuté čísla:", uhadnute)
print("Počet uhádnutých:", len(uhadnute))
# praca so súborom
subor = open("loteria_2.txt")
pocty = [0, 0, 0, 0, 0, 0, 0]

for riadok in subor:
    tipy = []
    for c in riadok.split():
        tipy.append(int(c))

    zhoda = 0
    for c in tipy:
        if c in zrebovane:
            zhoda += 1
    pocty[zhoda] += 1
subor.close()

print("Presne 1 číslo:", pocty[1])
print("Presne 2 čísla:", pocty[2])
print("Presne 3 čísla:", pocty[3])
print("Presne 5 čísel:", pocty[5])
print("Presne 6 čísel:", pocty[6])