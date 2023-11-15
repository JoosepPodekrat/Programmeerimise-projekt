import os
from datetime import date
def kuuPäev():
    täna = date.today()
    sisu = "Sissekanne "
    sõnum = sisu + str(täna)
    return sõnum
def avaFail(nimi):
    fail = open(nimi, encoding = "UTF=8")
    failsisu = fail.readlines()
    for rida in failsisu:
        if rida != "" :
            rida  = rida.strip()
            print(rida)
def loetleFailid(teefailideni):
    for(ketas, kaustad, file) in os.walk(teefailideni):
        for f in file:
            olemasolu = 1
            if ".txt" in f:
                print(f)
        if olemasolu != 1:
            print("Siin pole ühtegi .txt faili")
    return
def lisaSissekanne(nimi, märksõnad, sissekanne):
    try:
        failinimi = nimi + ".txt"
        with open(failinimi, "w", encoding="utf-8") as fail:
            fail.write(f"{nimi} - {märksõnad} - {sissekanne}\n")
            print("Sissekanne lisatud!")
    except FileNotFoundError:
        print(f"Faili {failinimi} ei leitud.")

def kustutaSissekanne(nimi):
    try:
        if os.path.isfile(nimi):
            os.remove(nimi)
            print("Sissekanne kustutatud!")
        else:
            print("Sellenimelist faili ei leitud, äkki jäi puudu .txt?")
    except FileNotFoundError:
        print(f"Faili {nimi} ei leitud.")


def main():
    while True:
        print("=== SINU PÄEVIK ===")
        print("Tee valik: ")
        print("Lisa uus sissekanne (L)")
        print("Kustuta sissekanne (K)")
        print("Lahku päevikust (E)")
        print("Loetle sissekanded (?)")
        print("Ava sissekanne (!)")
        
        valik = input("Valik: ").strip().upper()
        
        if valik == "L":
            failinimi = input("Sisesta sissekande nimi: ").strip()
            märksõnad = input("Sisesta mingid märksõnad enda sissekande kohta: ").strip()
            sissekanne = input("Kirjuta siia enda sissekanne: ").strip()
            lisaSissekanne(failinimi, märksõnad, sissekanne)
            
        elif valik == "K":
            sissekandeNimi = input("Sisesta sissekande nimi kustutamiseks: ")
            kustutaSissekanne(sissekandeNimi)
            
        elif valik == "E":
            break
        elif valik == "?":
            print("Päevikus on järgnevad sissekanded: ")
            path = os.getcwd()
            loetleFailid(path)
            print(" - - - ")
        elif valik == "!":
            print("Sissekande sisu on järmine: ")
            sisend = input("Palun sisestage sissekande nimi, mida tahate avada. ")
            print(" - - - ")
            avaFail(sisend)
            
            
        else:
            print("Vigane valik. Proovi uuesti :)")
        
if __name__ == "__main__":
    main()
