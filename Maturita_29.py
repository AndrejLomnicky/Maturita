def spracuj_riadok(riadok):
    vysledok = ""
    znak = "0"      # začíname počítaním núl
    pocet = 0
    for c in riadok:
        if c == znak:
            pocet += 1
        else:
            vysledok += str(pocet) + " "
            znak = c
            pocet = 1
    vysledok += str(pocet)
    return vysledok

with open("kompresia_obrazka_1.txt", encoding="cp1250") as fr:
    rozmery = fr.readline().split()
    sirka = int(rozmery[0])
    vyska = int(rozmery[1])
    print("Šírka:", sirka)
    print("Výška:", vyska)
    print("Počet bodov:", sirka * vyska)

    prvy = fr.readline().strip()
    print("Prvý riadok po spracovaní:", spracuj_riadok(prvy))

    riadky = [prvy]
    for riadok in fr:
        if riadok.strip() != "":
            riadky.append(riadok.strip())

with open("kompresia_obrazka_vystup.txt", "w", encoding="cp1250") as fw:
    fw.write(str(sirka) + " " + str(vyska) + "\n")
    for riadok in riadky:
        fw.write(spracuj_riadok(riadok) + "\n")