#príklad náhodné skúšanie
import random

pocet_studentov = int(input("Zadaj počet študentov: "))
pocet_otazok = int(input("Zadaj počet otázok: "))

if pocet_otazok < pocet_studentov:
    print("CHYBA: počet otázok je menší ako počet študentov!") # kontrola či je dostatok otázok
else:
    # náhodné poradie študentov (čísla 1 az pocet_studentov)
    studenti = list(range(1, pocet_studentov + 1))
    random.shuffle(studenti)

    # náhodné čísla otázok bez opakovania
    otazky = random.sample(range(1, pocet_otazok + 1), pocet_studentov)

    # vypísanie výsledku
    for i in range(pocet_studentov):
        print(f"Študent č. {studenti[i]} - otázka č. {otazky[i]}")