vstup = input("zadaj mi co idem heslovať:")
kluc = input("zadaj mi kluc")
#potrebujem spravit novy kluc
novy_kluc =kluc*(len(vstup)//len(kluc))+kluc[:len(vstup)%len(kluc):]   #dlzka kluca musi byt rovnaka dlzke klucu
vystup=""
for i in range(len(vstup)):
    if  97<=ord(vstup[i]) and ord(vstup[i])<=122:            #ak to co idem sifrovat je mala anglicka abeceda, az vtedy toto hujujubujuju
        posun = ord(novy_kluc[i])-96    # vstup[i] idem posunut o hodnotu ktora je v premennej posun
        vystup += chr((ord(vstup[i])-97 + posun)%26+97)  #toto nemusím zapísať do nového riadku
    else:
        vystup += vstup[i]
print(vystup)
#Maturitný príklad 23





