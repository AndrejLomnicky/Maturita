# zasifrovany text 2
import random
abeceda = "abcdefghijklmnopqrstuvwxyz"

def posun_text(text,posun):
    vysledok = ""
    for i in text:
        if i in abeceda:
            vysledok += abeceda[(abeceda.index(i) + posun) % 26]
        else:
            vysledok += i
    return vysledok

volba = input("Šifrovať (s) alebo dešifrovať (d)? ")

if volba == "s":
    vstup = open("vstupny_text.txt","r")
    vystup = open("zasifrovany_text_2.txt", "w",)
    for riadok in vstup:
        riadok = riadok.rstrip("\n")
        posun = random.randint(1, 25)
        vystup.write(abeceda[posun - 1] + posun_text(riadok, posun) + "\n")
else:
    vstup = open("zasifrovany_text_2.txt","r")
    vystup = open("desifrovany_text.txt", "w")
    for riadok in vstup:
        riadok = riadok.rstrip("\n")
        if riadok != "":
            posun = abeceda.index(riadok[0]) + 1
            vystup.write(posun_text(riadok[1:], -posun) + "\n")

vstup.close()
vystup.close()