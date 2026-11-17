#spokojnosť zákazníkov 1
with open("spokojnost_1.txt", "r",encoding="cp1250") as fr:
    riadky = fr.readlines()

# 1. celkový počet vyjadrení
pocet_vyjadreni = len(riadky)
print("celkový počet vyjadrení:", pocet_vyjadreni)

# zoznamy pre každú hodinu 0 až 23: koľko "áno" a koľko "nie"
ano = [0] * 24
nie = [0] * 24

for riadok in riadky:
    casti = riadok.split()            # napr. ['08:39', 'áno']
    hodina = int(casti[0].split(":")[0])   # '08:39' -> '08' -> 8
    if casti[1] == "áno":
        ano[hodina] += 1
    else:
        nie[hodina] += 1

# 2. hodina s najviac spokojnými zákazníkmi
max_ano = max(ano)
hodina_ano = ano.index(max_ano)
print("najviac spokojných zákazníkov bolo o", hodina_ano, "hodine, počet:", max_ano)

# 3. hodina s najviac nespokojnými zákazníkmi
max_nie = max(nie)
hodina_nie = nie.index(max_nie)
print("najviac nespokojných zákazníkov bolo o", hodina_nie, "hodine, počet:", max_nie)

# 4. percentá spokojnosti pre hodiny, ku ktorým existujú vyjadrenia
print("percentá spokojnosti:")
for hodina in range(24):
    spolu = ano[hodina] + nie[hodina]
    if spolu > 0:
        percento = ano[hodina] / spolu * 100
        print(hodina, "hod.:", round(percento, 1), "%")