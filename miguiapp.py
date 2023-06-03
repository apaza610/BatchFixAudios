#!/usr/bin/python3
import pathlib
import pygubu
import os
import tkinter as tk
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "migui.ui"
TEMPTXT = "D:/temp.txt"
TEMPTUTPATH = ""

class MiguiApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)

        self.taPathTutorial = builder.get_object("taPathTutorial")
        self.lblDebugMsg = builder.get_object("lblDebugMsg")

        import psutil
        if not "Audacity.exe" in (i.name() for i in psutil.process_iter()):
            self.lblDebugMsg.config(text = "Audacity is not opened !!")

    def run(self):
        self.mainwindow.mainloop()

    def batch_fix_audios(self):
        import tmptxt
        tmptxt.VIDSPATH = TEMPTUTPATH
        tmptxt.main()
    
    def clean_temp_txt(self):
        if os.stat(TEMPTXT).st_size == 0:
            os.remove("D:/temp.txt")
            self.lblDebugMsg.config(text = "temp.txt fue borrado")
        else:
            self.lblDebugMsg.config(text = "temp.txt not empty!!")

    def crear_temp_txt(self):
        with open(TEMPTXT, 'w')as fp:
            pass
        self.lblDebugMsg.config(text = "temp.txt fue creado")
        lNombres = []
        TEMPTUTPATH = self.taPathTutorial.get().replace('\\','/')
        # TEMPTUTPATH = TEMPTUTPATH
        self.taPathTutorial.delete(0, tk.END)
        self.taPathTutorial.insert(0, TEMPTUTPATH)
        # TEMPTUTPATH = self.taPathTutorial.get()
        for root, dirs, files in os.walk(TEMPTUTPATH):
            for filename in files:
                if os.path.splitext(filename)[1] == '.mp4':
                    elpath = os.path.join(root, filename).replace('\\','/')
                    if " " in elpath:
                        self.lblDebugMsg.config(text = "Err: space in name")
                        break
                    lNombres.append(elpath)
        import tmptxt
        tmptxt.write_temptxt(lNombres)

if __name__ == "__main__":
    app = MiguiApp()
    app.run()
    