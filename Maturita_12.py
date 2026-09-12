subor = open("bus_vytazenost.txt", "r", encoding="cp1250")
riadky = subor.readlines()
subor.close()

kapacita = int(riadky[0].strip())

zastavky = []
obsadenost = 0
preplnene_zastavky = []
najvyssi_prekrocenie = 0

for riadok in riadky[1:]:
    riadok = riadok.strip()
    casti = riadok.split()
    nastupujuci = int(casti[0])
    vystupujuci = int(casti[1])
    nazov = " ".join(casti[2:])

    zastavky.append(nazov)

    obsadenost = obsadenost - vystupujuci + nastupujuci

    if obsadenost > kapacita:
        preplnene_zastavky.append(nazov)
        prekrocenie = obsadenost - kapacita
        if prekrocenie > najvyssi_prekrocenie:
            najvyssi_prekrocenie = prekrocenie

print(f"Počet zastávok na trase: {len(zastavky)}")
print(", ".join(zastavky))

if preplnene_zastavky:
    print("Zastávky, kde bol autobus preplnený:", ", ".join(preplnene_zastavky))
    print(f"Najvyšší počet ľudí nad rámec kapacity: {najvyssi_prekrocenie}")
else:
    print("Autobus nebol na trase nikde preplnený.")