szel = 20
ar = []
meret = ["Kicsi", "Normál", "Nagy", ]
tipus = ["Sajtos", "Gombás", "Sonkás", ]
extra = ["Kukorica", "Sajt", "Bacon", "Nincs"]
tipus1 = []
meret1 = []
extra1 = ["Nincs"]
i = 0
def rendeles():
    print("Add meg a pizza adatait!")
    rendeles = input(" Szeretné a rendelést rögzít? i/n : ")
    if (rendeles == "i"):
        print(nyugta())
    elif (rendeles == "n"):
        print("A rendelés befejezéséhez kérem irjon egy @ jelet")
    elif ( rendeles == "@"):
        print("Köszönjük a rendelésést")
    else:
        print("Hibás adat bevitel")
    while (rendeles != "@"):
        rendeles = input("Akar új rendelést rögzíteni? i/n : ")
        if (rendeles == "i"):
            print(nyugta())
        elif(rendeles == "n"):
            print("A rendelés befejezéséhez kérem irjon egy @ jelet")
        elif (rendeles == "@"):
            print("Köszönjjük a rendelésést")
        else:
            print("Hibás adat bevitel")
    print(statisztika())

def nyugta():
    print("*" * szel)
    print(f"* 1 - {tipus[0]}       *")
    print(f"* 2 - {tipus[1]}       *")
    print(f"* 3 - {tipus[2]}       *")
    print("*" * szel)
    valasztas = input("Válasszon pizzát: ")
    if (valasztas == "1"):
            tipus1.append(tipus[0])
            ar.append(1000)
    elif (valasztas == "2"):
            tipus1.append(tipus[1])
            ar.append(1100)
    elif (valasztas == "3"):
            tipus1.append(tipus[2])
            ar.append(1200)
    else:
            print("Hibás adat bevitel")
    print("*" * szel)
    print(f"* 1 - {meret[0]}        *")
    print(f"* 2 - {meret[1]}       *")
    print(f"* 3 - {meret[2]}         *")
    print("*" * szel)
    valasztas1 = input("Válasszon méretet: ")
    if (valasztas1 == "1"):
            meret1.append(meret[0])
            ar[-1] = ar[-1] * 0.9
        #print(f"A Pizza ára {ar[0]}-FT")
    elif (valasztas1 == "2"):
            meret1.append(meret[1])
            ar[-1] = ar[-1] * 1
        #print(f"A Pizza ára {ar[1]}-FT")
    elif (valasztas1 == "3"):
            meret1.append(meret[2])
            ar[-1] = ar[-1] * 1.1
        #print(f"A Pizza ára {ar[2]}-FT")
    else:
            print("Hibás adat bevitel")
    valasztas2 = input("Kér extra feltétet? i/n : ")
    if (valasztas2 == "i"):
        print("*" * szel)
        print(f"* 1 - {extra[0]}     *")
        print(f"* 2 - {extra[1]}         *")
        print(f"* 3 - {extra[2]}        *")
        print("*" * szel)
        valasztas3 = input("Extra feltét válasszon kérem: ")
        if (valasztas3 == "1"):
            extra1.append(extra[0])
            ar[-1] = ar[-1] + 50
        elif (valasztas3 == "2"):
            extra1.append(extra[1])
            ar[-1] = ar[-1] + 50
        elif (valasztas3 == "3"):
            extra1.append(extra[2])
            ar[-1] = ar[-1] + 50
        else:
            print("Hibás adat bevitel")
    elif (valasztas2 == "n"):
        extra1.append(extra[3])
        print("Hát rendben")
    print(f"A rendelése egy {meret1[-1]} - {tipus1[-1]} pizza extra feltét - {extra1[-1]} Fizetendő: {ar[-1]}")


def statisztika():
    Sonkas = 0
    Gombas = 0
    Sajtos = 0
    x = 0
    while(x <= len(tipus1[:-1])):
        if (tipus1[x] == tipus[0]):
            Sajtos += 1
        elif (tipus1[x] == tipus[1]):
            Gombas += 1
        elif (tipus1[x] == tipus[2]):
            Sonkas += 1
        x = x + 1
    print(f"A Sajtos pizzából {Sajtos} fogyott")
    print(f"A Sonkas pizzából {Sonkas} fogyott")
    print(f"A Gombas pizzából {Gombas} fogyott")
    print(sum(ar))
