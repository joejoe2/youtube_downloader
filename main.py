from tkinter.ttk import Progressbar
from pytube import Stream
import dl
import tkinter as tk

win = tk.Tk()                          # 建立主視窗物件
win.geometry('640x480')
win.resizable(False, False)
win.title('pytube downloader')

# 設定網址輸入區域
input_frm = tk.Frame(win, width=640, height=50)
input_frm.pack()
# 設定提示文字
lb = tk.Label(input_frm, text='Type a link like https://www.youtube.com/watch?v=xxxxxxxxxxx', fg='black')
lb.place(rely=0.2, relx=0.5, anchor='center')
# 設定輸入框
input_url = tk.StringVar()     # 取得輸入的網址
input_et = tk.Entry(input_frm, textvariable=input_url, width=60)
input_et.place(rely=0.75, relx=0.5, anchor='center')

is_done = True
no = 0


# 設定按鈕
def btn_click():   # 按鈕的函式
    global is_done
    if not is_done:
        return
    else:
        global no
        is_done = False
        listbox.insert(no, "start")
        no += 1
        progress["value"] = 0
        result = dl.start(input_url.get(), show_progress_bar)
        listbox.insert(no, result + " at tmp/ folder")
        no += 1
        progress["value"] = 0
        is_done = True
        pass


def show_progress_bar(stream: Stream, chunk: bytes, bytes_remaining: int):
    print("{:00.0f}% downloaded".format((1-bytes_remaining/stream.filesize)*100))
    progress["value"] = int((1-bytes_remaining/stream.filesize)*100)
    progress.update()
    return


btn = tk.Button(input_frm, text='Download', command = btn_click,
                bg='orange', fg='Black')
btn.place(rely=0.75, relx=0.9, anchor='center')

# 下載清單區域
dl_frm = tk.Frame(win, width=640, height=280)
dl_frm.pack()
# 設定提示文字
lb = tk.Label(dl_frm, text='', fg='black')
lb.place(rely=0.1, relx=0.5, anchor='center')
# 設定顯示清單
listbox = tk.Listbox(dl_frm, width=65, height=15)
listbox.place(rely=0.6, relx=0.5, anchor='center')
# 設定捲軸
sbar = tk.Scrollbar(dl_frm)
sbar.place(rely=0.6, relx=0.87, anchor='center', relheight=0.75)
# 連結清單和捲軸
listbox.config(yscrollcommand = sbar.set)
sbar.config(command = listbox.yview)

# 設定提示文字
lb = tk.Label(win, text='progress', fg='black')
lb.place(rely=0.8, relx=0.25, anchor='center')
progress = Progressbar(win, orient=tk.HORIZONTAL, length=100, mode='determinate')
progress.place(rely=0.8, relx=0.5, anchor='center', relwidth=0.4)


# 啟動主視窗
win.mainloop()
