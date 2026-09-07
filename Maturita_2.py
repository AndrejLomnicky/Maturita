#háďa-priebeh hry
with open("hada.txt", "r") as subor:
    riadky = subor.readlines() #prečíta riadky
riadky = [riadok.strip() for riadok in riadky] #odstráni \n z konca

pocet_hier = len(riadky)  # len(riadky) spočíta koľko je riadkov
print("Počet hier:", pocet_hier)

dlzky = [len(riadok) for riadok in riadky] #spočita kolko je riadkov
najdlhsia_hra = max(dlzky) # vyberie najdlhší riadok
print("najdlhsia hra:", najdlhsia_hra)

with open("hada_kopia.txt", "w") as subor: # vytvorí kopiu hada,
    for riadok in riadky:
        subor.write(riadok + "\n")

with open("hada_komprimovane.txt", "w") as subor: # vytvori subor [H 4, L 6...]
    for riadok in riadky:
        vysledok = []
        aktualny_znak = riadok[0] #aktualny znak je ten na prvej čiže 0 pozicii
        pocitadlo = 0  # pocitadlo je na zaciatku 0

        for znak in riadok:  # prechádzame cyklom znaky v riadku
            if znak == aktualny_znak: # ked je znak ten isty ako aktualny znak(prvý znak)
                pocitadlo += 1  # pocitadlo sa zvacsi
            else:
                vysledok.append(aktualny_znak) # ked je znak iny ako aktualny znak tak pridam do zoznamu pismeno(aktualny znak a pocitadlo ako string)
                vysledok.append(str(pocitadlo))
                aktualny_znak = znak # vymenim za aktualny znak ten čo nasleduje
                pocitadlo = 1  # pocitadlo dam na 1 lebo som uz ten znak raz videl

        vysledok.append(aktualny_znak)
        vysledok.append(str(pocitadlo))

        komprimovany_riadok = " ".join(vysledok) #oddelím H a cislo medzerou
        subor.write(komprimovany_riadok + "\n") # napisem to tam aj s enterom
