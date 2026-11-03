import random
with open("virus.txt", encoding="cp1250") as fr:
    riadky = fr.read().splitlines()
print("Pôvodný text:")
for riadok in riadky:
    print(riadok)

if random.random() < 0.5:
    random.shuffle(riadky)

vystup = []
for riadok in riadky:
    slova = riadok.split(" ")
    if random.random() < 0.5:
        random.shuffle(slova)
    nove_slova = []
    for slovo in slova:
        if random.random() < 0.5:
            slovo = slovo[::-1]
        nove_slova.append(slovo)
    vystup.append(" ".join(nove_slova))

with open("virus_vystup.txt", "w", encoding="cp1250") as fw:
    fw.write("\n".join(vystup))
print("\nTransformovaný text:")
for riadok in vystup:
    print(riadok)