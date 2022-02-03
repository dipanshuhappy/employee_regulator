
from logger import listen_to_keyboard,get_total_keyboard_clicks
import mouse
from tkinter import *
total_mouse_moves=0
total_keyboard_clicks=0
window=Tk()
window.geometry("400x400")
label=Label(window, text="Keylogger is running")
label.pack()
def update_moves():
    global total_mouse_moves,total_keyboard_clicks
    total_mouse_moves=mouse.get_total_mouse_moves()
    total_keyboard_clicks=get_total_keyboard_clicks()
def show_log_info():
    update_moves()
    mouse_text=f"Total number of mouse moves are {total_mouse_moves}"
    Label(window,text=mouse_text).pack()
    keyboard_text=f"Total number of keyboard clicks are {total_keyboard_clicks}"
    Label(window,text=keyboard_text).pack()
window.after(3000,update_moves)
button=Button(window,text="Get logging info",command=show_log_info)
button.pack()
positions=[]
def get_mouse_pos():
    positions.append(window.winfo_pointerxy())
    mouse.write_to_file(positions)
    window.after(100, get_mouse_pos)
get_mouse_pos()
listen_to_keyboard()
window.mainloop()


