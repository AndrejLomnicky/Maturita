# tajna tabulka
#pismeno = "A" #priradi ordinalnu hodnotu
#ord(pismeno) - 65  # A->0
#(ord(pismeno) - 65) // 3 + 1 # ziskam skupinu do ktorej patri písmenko
#str((ord(pismeno) - 65) // 3 + 1) # z jednotky cislo mi to spravi jednotku znak
for n in "JOZO":
    print(str((ord(n) - 65) // 3 + 1)*((ord(n) - 65) % 3 + 1),end = " ")
