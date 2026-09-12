subor = open("sutaz_vbehu.txt", "r", encoding="utf-8")
riadky = subor.readlines()
subor.close()

mena = []
casy = []

for riadok in riadky:
    riadok = riadok.strip()
    casti = riadok.split()
    meno = casti[0]
    cas = int(casti[1])
    mena.append(meno)
    casy.append(cas)

print(f"Počet zúčastnených športovcov: {len(mena)}")

for i in range(len(mena)):
    print(f"Súťažiaci {mena[i]} dobehol do cieľa za {casy[i]} sekúnd")

najlepsi_cas = min(casy)
index_najlepsieho = casy.index(najlepsi_cas)
meno_vitaza = mena[index_najlepsieho]

minuty = najlepsi_cas // 60
sekundy = najlepsi_cas % 60

print(f"Víťazom sa stáva {meno_vitaza} s časom {minuty} min. {sekundy} sek.")