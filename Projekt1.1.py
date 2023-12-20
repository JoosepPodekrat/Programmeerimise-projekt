import tkinter as tk

class Guimain():
    def __init__(self, root):
        self.root = root
        self.ontume = False
        aktiivne_taust = "White"
        aktiivne_eesmine = "Black"
        #laud.attributes("-fullscreen", True)
        self.tume = {
            "bg":"white",
            "fg":"black",
            "entrybg" : "#eee",
            "entryfg" : "black",
            "buttonbg" : "#ddd",
            "buttonfg" : "black" ,
        }
        self.hele = {
            "bg" : "#eee",
            "fg" : "white",
            "entrybg" : "#555",
            "entryfg" : "white",
            "buttonbg" : "#444",
            "buttonfg" : "white",
        }
        self.label_pealkiri1 = tk.Label(root,text="Sinu päevik")
        self.label_pealkiri = tk.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        
        self.toggle_ontume = tk.Button(root,text="Vaheta tumeda versiooniga", command=self.vahetateema)
        self.toggle_ontume = tk.grid(row=0, column=5, padx=10, pady=10, sticky=tk.W)
        
        self.button_loetlefailid = tk.Button(root,text="Loetlefailid", command=self.loetlefailid)
        self.button_loetlefailid = tk.grid(row=2, column=5, padx=10, pady=10, sticky=tk.W)
        
        self.button_lisafail = tk.Label(root,text="lisa fail")
        self.button_lisafail = tk.grid(row=0, column=5, padx=10, pady=10, sticky=tk.W)
        
        self.entry_failinimi = tk.Entry(root)
        self.entry_failinimi = tk.grid(row=0, column=5, padx=10, pady=10, sticky=tk.W)
        
        self.button_kustutafail = tk.Button(root,text="Kustutafail", command=self.kustutafail)
        self.button_kustutafail = tk.grid(row=0, column=5, padx=10, pady=10, sticky=tk.W)
        
        
        
        
        
    def käivitateema(self, teema):
        self.root.config(bg=teema["bg"])
        for widget in self.root.winfo_children():
            widget_type = widget.winfo_class()
            if widget_type == "Label":
                widget.config(bg=theme["bg"], fg=theme["fg"])
            elif widget_type == "Entry":
                widget.config(bg=theme["entrybg"], fg=theme["entryfg"])
            elif widget_type == "Button":
                widget.config(bg=theme["buttonbg"], fg=theme["buttonfg"])
        
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
        
        self.pealkiri(pealkiri)
        self.geometry("300x100")
        self.config(bg=self.teema[bg])
        self.label = Tk.Label(self, text=message, bg=self.teema["bg"], fg=self.teema["fg"])
        self.button_ok = tk.Button(self, text="OK", bg=self.teema["buttonbg"], fg=self.teema["buttonfg"])
        