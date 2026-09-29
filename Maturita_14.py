krajiny = []
pocty = {}
najlepsi = 0
vitazi = []

with open("skok_do_dialky.txt") as subor:
    for riadok in subor:
        casti = riadok.split()
        if len(casti) == 0:
            continue

        meno = casti[0]
        krajina = casti[1]
        vykony = [int(x) for x in casti[2:7]]
        skok = max(vykony)


        if krajina not in pocty:
            krajiny.append(krajina)
            pocty[krajina] = 0
        pocty[krajina] += 1


        if skok > najlepsi:
            najlepsi = skok
            vitazi = [meno]
        elif skok == najlepsi:
            vitazi.append(meno)

print("Krajiny:", *krajiny)
print("Počty súťažiacich:")
for k in krajiny:
    print(k, pocty[k])
print("Víťaz:", *vitazi)