# pysum - pythonchecksum
# pysum uses the GPLv3 free license.
# Made by @tearsdev

from tkinterdnd2 import *
from tkinter import *
from tkinter import ttk
import subprocess
import pyperclip
import sys
import os
import webbrowser

root = TkinterDnD.Tk()

window_height = 250
window_width = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coords = int((screen_width / 2) - (window_width / 2))
y_coords = int((screen_height / 2) - (window_height / 2))

root.overrideredirect(True)
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coords, y_coords))
root.minsize(width=250, height=250)
root.maxsize(width=250, height=250)
root.minimized = False
root.maximized = False
root.config(bg="#25292e")

title_bar = Frame(root, bg='#10121f', relief='raised', bd=0, highlightthickness=0)


def set_appwindow(mainWindow):
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root.iconbitmap(resource_path("pysum.ico"))


def minimize_me():
    root.attributes("-alpha", 0)
    root.minimized = True


def deminimize(event):
    root.attributes("-alpha", 1)
    if root.minimized:
        root.minimized = False


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['foreground'] = self.defaultForeground


def opengit():
    webbrowser.open("https://github.com/tearsdev/pysum")


close_button = Button(title_bar, text='  ×  ', command=root.destroy, bg='#10121f', padx=2, pady=2, font=("calibri", 13),
                      bd=0, fg='white', highlightthickness=0)
minimize_button = Button(title_bar, text=' ‒ ', command=minimize_me, bg='#10121f', padx=2, pady=2, bd=0, fg='white',
                         font=("calibri", 13), highlightthickness=0)
title_bar_title = HoverButton(title_bar, command=opengit, bg='#10121f', bd=0, fg='white',
                              font=("Consolas Bold", 12),
                              highlightthickness=0, activeforeground='#3e4042')

window = Frame(root, bg='#25292e', highlightthickness=0)

title_bar.pack(fill=X)
close_button.pack(side=RIGHT, ipadx=7, ipady=1)
minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
title_bar_title.pack(side=LEFT, padx=10)
window.pack(expand=1, fill=BOTH)


def changex_on_hovering(event):
    global close_button
    close_button['bg'] = 'red'


def returnx_to_normalstate(event):
    global close_button
    close_button['bg'] = '#10121f'


def change_size_on_hovering(event):
    global expand_button
    expand_button['bg'] = '#3e4042'


def return_size_on_hovering(event):
    global expand_button
    expand_button['bg'] = '#10121f'


def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg'] = '#3e4042'


def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg'] = '#10121f'


def get_pos(event):
    if root.maximized == False:
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event):
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

        def release_window(event):
            root.config(cursor="arrow")

        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)


title_bar.bind('<Button-1>', get_pos)
title_bar_title.bind('<Button-1>', get_pos)

close_button.bind('<Enter>', changex_on_hovering)
close_button.bind('<Leave>', returnx_to_normalstate)
minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)

root.bind("<FocusIn>", deminimize)
root.after(10, lambda: set_appwindow(root))


def gets():
    global entri, comboget
    entri = entry.get()
    comboget = combo.get()


def gets2():
    global entri2
    entri2 = entry2.get()


def copy():
    pyperclip.copy(f"{newoutput[1]}")
    btn3.configure(text="✓ Copied")


def start():
    global newoutput, btn3, zxc
    gets()
    clear_frame()
    packtitle()
    output = subprocess.run(["certutil", "-hashfile", entri, comboget], stdout=subprocess.PIPE, text=True)
    newoutput = output.stdout.split("\n")
    zxc = Label(text=f"{newoutput[1]}", font=("Consolas Bold", 8), bg="#25292e", fg="white")
    title_bar_title.configure(text="pysum ✓")
    zxc.pack(expand=1)
    btn3.pack(expand=1)
    btn4.pack(expand=1)


def start2():
    gets()
    gets2()
    clear_frame()
    packtitle()
    output = subprocess.run(["certutil", "-hashfile", entri, comboget], stdout=subprocess.PIPE, text=True)
    newoutput = output.stdout.split("\n")
    lbl6 = Label(text="", font=("Consolas Bold", 12), bg="#25292e", fg="white")
    lbl6.pack(expand=1)
    if entri2 == newoutput[1]:
        title_bar_title.configure(text="pysum ✓")
        lbl6.configure(text=f"Checksums matches! \n The file is ok.")
    if entri2 != newoutput[1]:
        title_bar_title.configure(text="pysum X")
        lbl6.configure(text="Checksums doesn't match. \n The file is broken.")
    btn4.pack(expand=1)


def drop(event):
    entry_sv.set(event.data)


class Example(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.l1 = Label(self, text="Welcome to pysum", font=("Consolas Bold", 18), bg="#25292e", fg="white")
        self.l1.pack(side="top")

        self.l1.bind("<Enter>", self.on_enter)
        self.l1.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.l1.configure(text="1.0 | 2 June 2022")

    def on_leave(self, enter):
        self.l1.configure(text="Welcome to pysum", font=("Consolas Bold", 18), bg="#25292e", fg="white")


def getchecksum():
    clear_frame()
    packtitle()
    title_bar_title.configure(text="pysum #")
    backtomenu.pack(expand=1)
    lbl2.pack(expand=1)
    combo.pack(expand=1)
    lbl3.pack(expand=1)
    entry.pack(expand=1)
    begin.pack(expand=1)


def verifychecksum():
    global entry2, lbl5
    clear_frame()
    packtitle()
    title_bar_title.configure(text="pysum =")
    lbl5 = Label(text="Enter the checksum:", font=("Consolas", 15), bg="#25292e", fg="white", bd=0)
    entry2 = Entry(width=40, bg='#3e4042', fg="white", font=combofont, bd=0)
    backtomenu.pack(expand=1)
    lbl2.pack(expand=1)
    combo.pack(expand=1)
    lbl3.pack(expand=1)
    entry.pack(expand=1)
    lbl5.pack(expand=1)
    entry2.pack(expand=1)
    begin2.pack(expand=1)


combofont = ("Consolas Bold", 12)


def clear_frame():
    for widgets in root.winfo_children():
        widgets.forget()


def packtitle():
    title_bar_title.configure(text="pysum")
    title_bar.pack(fill=X)
    close_button.pack(side=RIGHT, ipadx=7, ipady=1)
    minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
    title_bar_title.pack(side=LEFT, padx=10)
    window.pack(expand=1, fill=BOTH)


def menu():
    global lbl, btn, btn2, btn3, btn4
    clear_frame()
    packtitle()
    Example(root).pack(expand=1)
    btn = HoverButton(root, text="# Get checksum", command=getchecksum, font=("Corbel Bold", 20), bg="#25292e",
                      fg="white", bd=0, activeforeground='#3e4042')
    btn.pack(expand=1)
    btn2 = HoverButton(root, text="= Verify checksum", command=verifychecksum, font=("Corbel Bold", 20), bg="#25292e",
                       fg="white", bd=0, activeforeground='#3e4042')
    btn2.pack(expand=1)


style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground='#3e4042', background='#3e4042', foreground='white')
root.option_add("*TCombobox*Listbox*Background", '#25292e')
root.option_add('*TCombobox*Listbox*Foreground', 'white')
combo = ttk.Combobox(root, width=39, font=combofont,
                     values=["SHA1", "SHA256", "SHA384", "SHA384", "SHA512", "MD2", "MD4", "MD5"])
combo.current(7)

btn4 = HoverButton(root, bd=0, activeforeground='#3e4042', text="⌂ Go to menu", command=menu, font=("Corbel Bold", 15),
                   bg="#25292e", fg="white")
btn3 = HoverButton(root, bd=0, activeforeground='#3e4042', text="✎ Copy checksum", command=copy,
                   font=("Corbel Bold", 15),
                   bg="#25292e", fg="white")
begin = HoverButton(root, bd=0, activeforeground='#3e4042', text="▶ Start", command=start, font=("Corbel Bold", 15),
                    bg="#25292e", fg="white")
begin2 = HoverButton(root, bd=0, activeforeground='#3e4042', text="▶ Start", command=start2, font=("Corbel Bold", 15),
                     bg="#25292e", fg="white")
backtomenu = HoverButton(root, text="◀ Back to menu", command=menu, font=("Corbel Bold", 10), bg="#25292e", fg="white",
                         bd=0, activeforeground='#3e4042')

lbl2 = Label(text="Select hash type:", font=("Consolas", 15), bg="#25292e", fg="white")
lbl3 = Label(text="Enter file's path:", font=("Consolas", 15), bg="#25292e", fg="white")

entry_sv = StringVar()
entry = Entry(textvar=entry_sv, width=40, bg='#3e4042', fg="white", font=combofont, bd=0)

entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)

menu()
root.mainloop()
