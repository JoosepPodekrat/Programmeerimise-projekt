import os
from datetime import date

def kuuPäev():
    täna = date.today()
    sisu = "Sissekanne "
    sõnum = sisu + str(täna)
    return sõnum
def kustutaFail(failinimi):
    if os.path.isfile(failinimi):
        os.remove(failinimi)
    return ("Kustutasin faili")

def loetleFailid(teefailideni):
    tee = teefailideni
    for(ketas, kaustad, file) in os.walk(tee):# vajab r"path" vormistust, loetleFailid(r"C:\Users\podekrat\Documents\Thonny Kodutööd") töötab, v normaliseerida \ /ideks
        for f in file:
            olemasolu = 1
            if ".txt" in f:
                print(f)
        if olemasolu != 1:
            print("Siin pole ühtegi .txt faili")
    return
        

def avaFail(failinimi):
    fail = open(failinimi, encoding = "UTF=8")
    failsisu = fail.readlines()
    for rida in failsisu:
        if rida != "" :
            rida  = rida.strip()
            print(rida)
    else:
        return
    fail.close()
    return

def kirjutaFail(sisutekst):
    failinimi = kuuPäev() + ".txt"
    fail = open(failinimi, "w", encoding = "UTF=8")
    fail.write("\n" + sisutekst)
    fail.close()
    return failinimi

def muudaPath(uuspath):
    return