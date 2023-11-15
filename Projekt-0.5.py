def lisaSissekanne(nimi, märksõnad, sissekanne):
    try:
        with open(nimi, "w", encoding="utf-8") as fail:
            fail.write(f"{nimi} - {märksõnad} - {sissekanne}\n")
            print("Sissekanne lisatud!")
    except FileNotFoundError:
        print(f"Faili {failinimi} ei leitud.")

def kustuta_sissekanne(nimi, märksõnad, sissekanne):
    try:
        with open(failinimi, "r", encoding="utf-8") as fail:
            sissekanded = fail.readlines()

        with open(failinimi, "w", encoding="utf-8") as fail:
            for rida in sissekanded:
                if nimi not in rida:
                    fail.write(rida)
            print("Sissekanne kustutatud!")
    except FileNotFoundError:
        print(f"Faili {failinimi} ei leitud.")


def main():
    while True:
        print("=== SINU PÄEVIK ===")
        print("Tee valik: ")
        print("Lisa uus sissekanne (L)")
        print("Kustuta sissekanne (K)")
        print("Lahku päevikust (E)")
        
        valik = input("Valik: ").strip().upper()
        
        if valik == "L":
            failinimi = input("Sisesta sissekande nimi: ").strip()
            märksõnad = input("Sisesta mingid märksõnad enda sissekande kohta: ").strip()
            sissekanne = input("Kirjuta siia enda sissekanne: ").strip()
            lisaSissekanne(failinimi, märksõnad, sissekanne)
            
        elif valik == "K":
            sissekande_nimi = input("Sisesta sissekande nimi kustutamiseks: ")
            kustutaSissekanne(nimi, märksõnad, sissekanne)
            
        elif valik == "E":
            break
        else:
            print("Vigane valik. Proovi uuesti :)")
        
if __name__ == "__main__":
    main()
