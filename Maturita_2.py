#háďa-priebeh hry
with open("hada.txt", "r") as subor:
    riadky = subor.readlines()
riadky = [riadok.strip() for riadok in riadky]

pocet_hier = len(riadky)
print("Počet hier:", pocet_hier)

dlzky = [len(riadok) for riadok in riadky]
najdlhsia_hra = max(dlzky)
print("najdlhsia hra:", najdlhsia_hra)

with open("hada_kopia.txt", "w") as subor:
    for riadok in riadky:
        subor.write(riadok + "\n")

with open("hada_komprimovane.txt", "w") as subor:
    for riadok in riadky:
        vysledok = []
        aktualny_znak = riadok[0]
        pocitadlo = 0

        for znak in riadok:
            if znak == aktualny_znak:
                pocitadlo += 1
            else:
                vysledok.append(aktualny_znak)
                vysledok.append(str(pocitadlo))
                aktualny_znak = znak
                pocitadlo = 1

        vysledok.append(aktualny_znak)
        vysledok.append(str(pocitadlo))

        komprimovany_riadok = " ".join(vysledok)
        subor.write(komprimovany_riadok + "\n")
