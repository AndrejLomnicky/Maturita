#hlasovanie 2
with open("hlasovanie_1.txt", "r") as fr:
    riadky = fr.readlines()

pocet_sms = len(riadky)
print("celkový počet SMS:", pocet_sms)

# pre každé číslo súťažiaceho 5220 až 5229 vytvoríme jeden súbor
for cislo in range(5220, 5230):
    with open(str(cislo) + ".txt", "w") as fw:
        for poradie in range(1, pocet_sms + 1):
            if riadky[poradie - 1].strip() == str(cislo):
                fw.write(str(poradie) + "\n")