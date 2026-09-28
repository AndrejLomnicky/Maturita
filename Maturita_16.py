# príklad mena v stlpcoch
fr = open("mena_zamestnancov.txt","r")
fw = open("vysledok.txt","w")
zoz = fr.readlines()
zoz_pol = zoz[:len(zoz)//2]
zoz_pol2 = zoz_pol[(len(zoz)//2)+1:]
max_retazec = zoz_pol[0]

for i in range(1,len(zoz_pol)):
    if len(zoz_pol[i]) > len(max_retazec):
        max_retazec = zoz_pol[i]

for i in range(len(zoz_pol)):
    fw.write(zoz_pol[i] + " "*(len(max_retazec)-len(zoz_pol[i])))
fr.close()





