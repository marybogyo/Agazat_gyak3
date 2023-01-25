import random
szam_lista = []
def veltelen():
    i = 0
    szov_lista = ""
    while i < 15:
        vel = int(random.random() * 591) - 90
        szam_lista.append(vel)
        if i == 14:
            szov_lista += str(vel) + ""
        else:
            szov_lista += str(vel) + "*"
        i += 1
    print(f"II/A, B, C:\n\t{szov_lista}")


def oszthatoak_szama():
    i = 0
    oszthatodb = 0
    while i < len(szam_lista):
        if (szam_lista[i] % 10 == 0):
            oszthatodb += 1
        i += 1

    return oszthatodb


def konzolra_ir():
    print(f"II/D, E:\n\t Tízzel osztható számok száma: {oszthatoak_szama()}")


def fajl_ir():
    fajl = open("eredmeny.txt", "w", encoding="utf-8")
    fajl.write(f"II/F\n\t Tízzel osztható számok száma: {oszthatoak_szama()}")
    fajl.close()
