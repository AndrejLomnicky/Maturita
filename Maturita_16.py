# priklad mena v stlpcoch
fr = open("mena_zamestnancov.txt","r")
fw = open("vystup.txt","w")
zoz = fr.readlines()
pol = len(zoz)//2
mena = zoz[:pol]
priezviska = zoz[pol:]

for i in range(pol):
    mena[i] = mena[i].strip()
    priezviska[i] = priezviska[i].strip()

max_meno = mena[0]
for i in range(1,pol):
    if len(mena[i]) > len(max_meno):
        max_meno = mena[i]

max_priez = priezviska[0]
for i in range(1,pol):
    if len(priezviska[i]) > len(max_priez):
        max_priez = priezviska[i]

print("Počet mien:", pol)
print("Dĺžka najdlhšieho krstného mena:", len(max_meno))
print("Dĺžka najdlhšieho priezviska:", len(max_priez))

for i in range(pol):
    fw.write(mena[i] + " "*(len(max_meno)-len(mena[i])) + " " + priezviska[i] + "\n")

fr.close()
fw.close()





