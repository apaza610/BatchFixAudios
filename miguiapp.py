#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "migui.ui"


class MiguiApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)

        self.taPathTutorial = builder.get_object("taPathTutorial")

    def run(self):
        self.mainwindow.mainloop()

    def batch_fix_audios(self):
        print("has presionado boton")
        import principal
        principal.PATHTUTORIAL = self.taPathTutorial.get()
        print("........comenzando conversion.........")
        principal.catch_mp4s()

if __name__ == "__main__":
    app = MiguiApp()
    app.run()
    