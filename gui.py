from tkinter import Tk, Frame, Button, Entry, END, Label
from tkinter.ttk import Progressbar
from dl import yt_downloader
import os
import threading
from pwindow import pwnd


class app(Frame):
    def __init__(self, ruler=Tk(className="yt mp4 downloader")):
        ruler.geometry("300x300")  # You want the size of the app to be 500x500
        ruler.resizable(0, 0)  # Don't allow resizing in the x or y direction
        Frame.__init__(self, ruler)
        self.tk = self.master.tk
        self.pack()
        self.makeComponent()
        pass

    def makeComponent(self):
        self.checkbtn = Button(self)
        self.checkbtn["text"] = "check link"
        self.checkbtn["command"] = self.check
        self.checkbtn.pack(side="left")

        self.DLBtn = Button(self, text="DL", fg="blue", command=self.threadstart)
        self.DLBtn.pack(side="right")

        self.txt = Entry(self)
        self.txt.pack(side="left")

        self.label = Label()
        self.label["text"] = "mode : best mp4 video + audio" + "\n" \
                             + "url format = \n https://www.youtube.com/watch?v=xxxxxxxxx"
        self.label.place(x=20, y=100)
        pass

    def check(self):
        url = str(self.txt.get())
        print("checking " + url)

        if (url.startswith("https://www.youtube.com/watch?v=")) and ("&" not in url):
            print("format check success")
            pass
        else:
            print("format check fail, please to be " + "https://www.youtube.com/watch?v=xxxxxxxxx  like format")
            self.txt.delete(0, END)
            pass

        pass

    def threadstart(self):
        threading.Thread(target=self.download).start()
        pass

    def download(self, option="mp4 best v+a"):
        ytdl = yt_downloader()
        # p = pwnd(ruler=work)
        # p.pack(side="bottom")
        title, l = ytdl.find(url=str(self.txt.get()), opt=option)
        self.txt.delete(0, END)
        title = title.replace("/", " ").replace("\\", " ").replace("*", " ").replace(":", " ") \
            .replace("?", " ").replace("\"", " ").replace("<", " ").replace(">", " ").replace("|", " ")
        f = []
        i = 0
        for item in l:
            i = i + 1
            f.append(ytdl.download(item, str(i) + "tmp" + str(title.__hash__()), ".mp4"))
        if f.__len__() == 2:
            ytdl.merge(f[1], f[0], out="tmp\\" + str(title.__hash__()) + ".mp4")
            os.remove(f[0])
            os.remove(f[1])
            os.replace("tmp\\" + str(title.__hash__()) + ".mp4", "tmp\\" + title + ".mp4")
        print("done")
        pass


"https://www.youtube.com/watch?v=G9nHP6aRsjE"

print("initializing gui...")
print("...................")
print("please do not close this window if you do not want to exit the program !!!")
print()
print()
print()
work = app()
work.lift()
print("gui build up complete")
print("please do not close this window if you do not want to exit the program !!!")
print()
work.mainloop()

