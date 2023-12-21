import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import os
from datetime import date
class Guimain():
    def __init__(self, root):
        self.root = root
        a = "600"
        b = "400"
        root.geometry(a + "x" + b)
        self.ontume = True
        self.tume = {
            "bg":"white",
            "fg":"black",
            "entrybg" : "#eee",
            "entryfg" : "black",
            "buttonbg" : "#ddd",
            "buttonfg" : "black" ,
        }
        self.hele = {
            "bg" : "#444",
            "fg" : "white",
            "entrybg" : "#444",
            "entryfg" : "white",
            "buttonbg" : "#444",
            "buttonfg" : "white",
        }
        self.label_pealkiri = tk.Label(root,text="Sinu päevik")
        self.label_pealkiri.grid(row=0, column=0, padx=10, pady=10, sticky="WNE")
        
        self.toggle_ontume = tk.Button(root,text="Dark mode", command=lambda: self.vahetateema())
        self.toggle_ontume.grid(row=5, column=0, padx=10, pady=10, sticky="W")
        
        self.button_loetlefailid = tk.Button(root,text="Loetlefailid", command=lambda: self.loetlefailid())
        self.button_loetlefailid.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        
        self.button_avafail_start = tk.Button(root,text="Ava fail", command=lambda: self.avafail_start())
        self.button_avafail_start.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        
        self.button_lisafail_start = tk.Button(root,text="lisa fail", command=lambda: self.lisafail_start())
        self.button_lisafail_start.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        
        
        self.button_kustutafail_start = tk.Button(root,text="Kustutafail", command=lambda: self.kustutafail_start())
        self.button_kustutafail_start.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        
    def avafail_start(self):
        self.label_selgitus1 = tk.Label(root,text="Failinimi:")
        self.label_selgitus1.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.button_avafail_start.destroy()
        self.entry_failinimi_ava = tk.Entry(root)
        self.entry_failinimi_ava.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        self.button_avafail = tk.Button(root,text="Kinnita ava", command=lambda: self.avafail(self.entry_sisu(self.entry_failinimi_ava)))
        self.button_avafail.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.käivitateema(self.tume if self.ontume else self.hele)
        
        
        pass
    def avafail(self,nimi):
        self.label_selgitus1.destroy()
        self.button_avafail.destroy()
        self.entry_failinimi_ava.destroy()
        self.button_avafail_start = tk.Button(root,text="Ava fail", command=lambda: self.avafail_start())
        self.button_avafail_start.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        try:
            fail = open(nimi, encoding = "UTF=8")
            failsisu = fail.readlines()
            failisisu = []
            for rida in failsisu:
                if rida != "" :
                    rida  = rida.strip()
                    print(rida)
                    failisisu.append(rida)
            try:
                self.label_failisisu.destroy()
            except:
                pass
        except FileNotFoundError:
            CMessagebox(self.root, "ERROR", "Sisesta korrektne failinimi entry alale.", self.tume if self.ontume else self.hele)
        
        self.label_failisisu = tk.Label(root, text = failisisu, bg='white', relief='groove', wraplength=250)
        self.label_failisisu.grid(row=1, column=10, columnspan=9, pady=1.25, sticky="sew")
        self.käivitateema(self.tume if self.ontume else self.hele)
    def loetlefailid(self):
        teefailideni = os.getcwd()
        sõnumlist = []
        for(ketas, kaustad, file) in os.walk(teefailideni):
            for f in file:
                olemasolu = 1
                if ".txt" in f:
                    sõnumlist.append(f+"\n")
        if olemasolu != 1:
            CMessagebox(self.root, "Failisisu", "Siin kaustas ei leidunud .txt faile", self.tume if self.ontume else self.hele)
        else:
            CMessagebox(self.root, "Failisisu on", sõnumlist, self.tume if self.ontume else self.hele)
        self.käivitateema(self.tume if self.ontume else self.hele)
    
    def entry_sisu(self, entrynimi):
        sisu = entrynimi.get()
        return sisu
    
    def kustutafail_start(self):
        self.label_selgitus1 = tk.Label(root,text="Failinimi:")
        self.label_selgitus1.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.button_kustutafail_start.destroy()
        self.entry_failinimi = tk.Entry(root)
        self.entry_failinimi.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)
        self.button_kustutafail = tk.Button(root,text="Kinnita kustuta", command=lambda: self.kustutafail(self.entry_sisu(self.entry_failinimi)))
        self.button_kustutafail.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.käivitateema(self.tume if self.ontume else self.hele)
        
    def kustutafail(self, nimi):
        self.label_selgitus1.destroy()
        self.button_kustutafail.destroy()
        self.entry_failinimi.destroy()
        self.button_kustutafail_start = tk.Button(root,text="Kustutafail", command=self.kustutafail_start)
        self.button_kustutafail_start.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.käivitateema(self.tume if self.ontume else self.hele)
        try:
            if os.path.isfile(nimi):
                os.remove(nimi)
                CMessagebox(self.root, "Kustuta fail", "Sellenimeline fail on kustutatud.", self.tume if self.ontume else self.hele)
            else:
                CMessagebox(self.root, "ERROR", "Sellenimelist faili ei leitud.", self.tume if self.ontume else self.hele)
        except TypeError:
            CMessagebox(self.root, "ERROR", "Sisesta korrektne failinimi entry alale.", self.tume if self.ontume else self.hele)
        pass
    def lisafail_start(self):
        self.label_selgitus1 = tk.Label(root,text="Failinimi")
        self.label_selgitus1.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.label_selgitus2 = tk.Label(root,text="Faili sisu:")
        self.label_selgitus2.grid(row=1, column=2, padx=10, pady=10, sticky="W")
        print("Lisafail")
        self.button_lisafail_start.destroy()
        self.button_lisafail = tk.Button(root,text="Kinnita lisa", command=lambda: self.lisafail())
        self.button_lisafail.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_failinimi_lisa = tk.Entry(root)
        self.entry_failinimi_lisa.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
        self.entry_failisisu_lisa = tk.Entry(root)
        self.entry_failisisu_lisa.grid(row=3, column=2, padx=10, pady=10, sticky=tk.W)
        self.käivitateema(self.tume if self.ontume else self.hele)
        pass
    def lisafail(self):
        try:
            failinimi = self.entry_sisu(self.entry_failinimi_lisa)
            sisu = self.entry_sisu(self.entry_failisisu_lisa)
            with open(failinimi, "w", encoding="utf-8") as fail:
                fail.write(sisu)
                CMessagebox(self.root, "Fail", "Fail salvestatud.", self.tume if self.ontume else self.hele)
        except FileNotFoundError:
            CMessagebox(self.root, "ERROR", "Sisesta korrektne failinimi entry alale.", self.tume if self.ontume else self.hele)
        self.button_lisafail.destroy()
        self.label_selgitus1.destroy()
        self.label_selgitus2.destroy()
        self.entry_failinimi_lisa.destroy()
        self.entry_failisisu_lisa.destroy()
        self.button_lisafail_start = tk.Button(root,text="lisa fail", command=lambda: self.lisafail_start())
        self.button_lisafail_start.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.käivitateema(self.tume if self.ontume else self.hele)
        
        
        
        
        
    def käivitateema(self, teema):
        self.root.config(bg=teema["bg"])
        for widget in self.root.winfo_children():
            widget_type = widget.winfo_class()
            if widget_type == "Label":
                widget.config(bg=teema["bg"], fg=teema["fg"])
            elif widget_type == "Entry":
                widget.config(bg=teema["entrybg"], fg=teema["entryfg"])
            elif widget_type == "Button":
                widget.config(bg=teema["buttonbg"], fg=teema["buttonfg"])
        
    def vahetateema(self):
        if self.ontume:
            self.käivitateema(self.hele)
        else:
            self.käivitateema(self.tume)
        self.ontume = not self.ontume
class CMessagebox(tk.Toplevel):
    
    def __init__(self, vanem, pealkiri, sõnum, teema):
        super().__init__(vanem)
        self.teema = teema
        
        self.pealkiri = pealkiri
        self.geometry("300x100")
        self.config(bg=self.teema["bg"])
        self.label = tk.Label(self, text=sõnum, bg=self.teema["bg"], fg=self.teema["fg"])
        self.label.pack(padx=20, pady=20)
        self.button_ok = tk.Button(self, text="OK", bg=self.teema["buttonbg"], fg=self.teema["buttonfg"], command=self.destroy)
        self.button_ok.pack(pady=10)

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=4)
root.title("Sinu Päevik")
app = Guimain(root)
root.mainloop()
        
