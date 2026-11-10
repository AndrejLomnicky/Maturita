#konverzia súboru 1
with open("ciernobiely_obrazok_1.txt", "r") as fr:
    riadky = fr.readlines()
rozmery = riadky[0].split()
sirka = int(rozmery[0])
vyska = int(rozmery[1])
pocet_bodov = sirka*vyska
print("šírka:",sirka)
print("výška:",vyska)
print("počet bodov:",pocet_bodov)
vysledok = []
def spracuj_riadok(riadok):
    for i in range(0, len(riadok),2):
        dvojica = int(riadok[i:i+2],16)
        if dvojica < 128:
            vysledok.append("0")
        else:
            vysledok.append("1")
    return " ".join(vysledok)
prvy_riadok = riadky[1].strip()
print("prvý riadok:",spracuj_riadok(prvy_riadok))

with open("konverzia_suboru_1_vystup.txt", "w") as fw:
    fw.write(f"{sirka} {vyska}\n")
    vysledok_2 = []
    for x in range(1, len(riadky)):
        vsetky = riadky[x].strip()
        spracovane = spracuj_riadok(vsetky)
        vysledok.append(spracovane)
        fw.write(f"{spracovane}\n")






