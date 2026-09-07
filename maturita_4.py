# úloha meteorologické stanice
with open("meteo_stanice.txt") as subor: # otvorime textovy subor meteostanice
    riadky = subor.readlines() # precitame riadky

zaznamy = [riadok.split() for riadok in riadky]  # pomocou komprehensie a split vytvorime zaznamy
teploty = [float(zaznam[3].replace(",", ".")) for zaznam in zaznamy] # vymenime ciarku za bodku a vyberieme zaznam teplot na 3 indexe, dáme ho ako float pouziheme komprehensiu

print("Počet meraní:", len(zaznamy))  # pocet merani je pocet riadkov
print("Namerané teploty:", teploty)    # vypise vsetky teploty(indexy[3]) ako zoznam

najvyssia = max(teploty) # funkcia max zistí najvyssiu nameranú teplotu

priemer = sum(teploty) / len(teploty)  # priemer = teploty spocitame/kolko je merani

index_najvyssej = teploty.index(najvyssia) # zistime index stanice s najvyssou teplotou
kod_stanice = zaznamy[index_najvyssej][0]  # vypiseme index stanice s najvyssou teplotou

print("Najvyššia teplota:", najvyssia)
print("Kód stanice s najvyššou teplotou:", kod_stanice)
print("Priemerná teplota:", priemer)