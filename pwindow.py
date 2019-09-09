from tkinter import Tk, Frame, HORIZONTAL
from tkinter.ttk import Progressbar


class pwnd(Frame):
    def __init__(self, ruler):
        Frame.__init__(self, ruler)
        self.makeComponent()
        pass

    def makeComponent(self):
        self.progressbar = Progressbar(self, length=200, mode="determinate", orient=HORIZONTAL)
        self.progressbar.pack(side="top")

    def setprogress(self, value):
        self.progressbar["value"] = str(value)
    pass
