#spokojnosť zákazníkov 2
with open("spokojnost_1.txt", "r", encoding="cp1250") as fr:
    riadky = fr.readlines()

hodiny = [0] * 24      # počet vyjadrení v jednotlivých hodinách
dni = []               # počet vyjadrení v jednotlivých dňoch
predchadzajuci = -1    # čas predchádzajúceho vyjadrenia v minútach

for riadok in riadky:
    casti = riadok.split()                 # napr. ['15:38', 'áno']
    if len(casti) == 0:                    # preskočí prázdny riadok
        continue
    cas = casti[0].split(":")
    hodina = int(cas[0])
    minuta = int(cas[1])
    minuty = hodina * 60 + minuta          # čas prepočítaný na minúty

    # ak je čas menší ako predchádzajúci, začal sa nový deň
    if minuty < predchadzajuci or len(dni) == 0:
        dni.append(0)

    dni[-1] += 1
    hodiny[hodina] += 1
    predchadzajuci = minuty

# výpis počtu reakcií v jednotlivých dňoch
for i in range(len(dni)):
    print(str(i + 1) + ". deň - počet reakcii:" + str(dni[i]))

# celkový počet vyjadrení
print("Počet všetkých vyjadrení:", sum(dni))

# počet vyjadrení v hodinách, kde nejaké boli
for hodina in range(24):
    if hodiny[hodina] > 0:
        print("Hodina:" + str(hodina), "Reakcii zákazníkov:" + str(hodiny[hodina]))

# počet dní
print("Počet dní:", len(dni))