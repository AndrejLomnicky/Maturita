#dekompresia obrázka
with open("dekompresia_obrazka_1.txt", "r") as fr:
    riadky = fr.readlines()

rozmery = riadky[0].split()
sirka = int(rozmery[0])
vyska = int(rozmery[1])
pocet_bodov = sirka * vyska
print("šírka:", sirka)
print("výška:", vyska)
print("počet bodov:", pocet_bodov)

def spracuj_riadok(riadok):
    cisla = riadok.split()
    vysledok = ""
    farba = "0"                      # riadok vždy začína čiernymi bodmi (0)
    for cislo in cisla:
        vysledok = vysledok + farba * int(cislo)
        if farba == "0":             # striedanie farby
            farba = "1"
        else:
            farba = "0"
    return vysledok

prvy_riadok = riadky[1].strip()
print("prvý riadok:", spracuj_riadok(prvy_riadok))

with open("dekompresia_obrazka_vystup.txt", "w") as fw:
    fw.write(f"{sirka} {vyska}\n")
    for x in range(1, len(riadky)):
        hodnoty = riadky[x].strip()
        spracovany = spracuj_riadok(hodnoty)
        fw.write(spracovany + "\n")