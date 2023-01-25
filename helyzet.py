from Gepek_PC import Gepek_PC
gep_lista = []
def beolvas():
    fajl = open("gep.txt", "r", encoding="utf-8")
    fajl.readline()
    gepek = fajl.readlines()
    fajl.close()
    #print(gepek)

    i = 0
    while i < len(gepek):
        gep = gepek[i].strip().split("!")
        gep_lista.append(Gepek_PC(gep))
        i += 1


def gep_szam():

    print(f"III/A, B:\n\t A gépek száma: {len(gep_lista)}")


def terem():
    i = 0
    hely = []
    hely_db = 0
    hely_ossz = 0
    while i < len(gep_lista):
        terem_szam = gep_lista[i].hely.split("T")[1]
        hely.append(terem_szam)
        if (int(hely[i]) % 2 == 0):
            hely_db += 1
            hely_ossz += int(hely[i])

        i += 1
    atlag = hely_ossz / hely_db

    print(f"III/C:\n\t A páros teremszámú termek azonosító átlaga: {atlag:.2f}")

def lekisebb_gep():
    i = 0
    legkisebb = gep_lista[0]
    while i < len(gep_lista):
        if (gep_lista[i].id < legkisebb.id):
            legkisebb = gep_lista[i]
        i += 1
    return legkisebb

