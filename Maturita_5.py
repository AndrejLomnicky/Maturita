# príklad objednané jedlá
with open("objednane_jedla.txt") as subor:
    riadky = subor.readlines()

zaznamy = [riadok.split() for riadok in riadky]

pocet_jedal = len(zaznamy)
print("Počet objednaných jedál:", pocet_jedal)

farby = [zaznam[1] for zaznam in zaznamy]
pocet_zelena = farby.count('z')
pocet_cervena = farby.count('c')
pocet_modra = farby.count('m')
pocet_oranzova = farby.count('o')

print("Zelená:", pocet_zelena)
print("Červená:", pocet_cervena)
print("Modrá:", pocet_modra)
print("Oranžová:", pocet_oranzova)

pocty = { 'z': pocet_zelena,'c': pocet_cervena,'m': pocet_modra,'o': pocet_oranzova}

vsetko_ok = True

for farba, pocet in pocty.items():
    if pocet < 20:
        print("Jedlo s nedostatkom objednávok:", farba)
        vsetko_ok = False

if vsetko_ok:
    print("Všetky jedlá si objednalo dostatok stravníkov.")