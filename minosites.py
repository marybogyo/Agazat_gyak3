def muzeum():
    muzeum_nev = input(f"I/A:\n \t Múzeum neve: ")
    latogato = input("\t Látogató neve: ")
    ertek = int(input("\t Értékelés: "))
    if ertek <= 0:
        print(f"I/B:\n \t Az értékelés nem lehet negatív vagy 0!")
    elif ertek > 20:
        print(f"I/B:\n \t 20 pont feletti értékelés nem elfogadható!")
    else:
        print(f"I/B:\n \t Köszönjük az értkelést!")

    print(f"I/A:\n \t Múzeum neve:{muzeum_nev}\n \t Látogató neve:{latogato}\n \t Értékelés:{ertek}\n I/B:\n \tKöszönjük az értékelést! ")
