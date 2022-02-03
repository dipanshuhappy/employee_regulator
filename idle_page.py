from logger import listen_to_keyboard,get_total_keyboard_clicks
import mouse
from tkinter import *
total_mouse_moves=0
total_keyboard_clicks=0
window=Tk()
window.geometry("400x400")
label=Label(window, text="Keylogger is running")
label.pack()
def idle_or_not():
    new_keyboard=get_total_keyboard_clicks()
    print(f'old_keyboard_click:{total_keyboard_clicks} and  new {new_keyboard}')
    new_mouse=mouse.get_total_mouse_moves()
    print(f'total mouse :{total_mouse_moves} and new {new_mouse}')
    idle=total_keyboard_clicks==new_keyboard and total_mouse_moves==new_mouse
    print(idle)
    text=f'You are idle {idle}'
    Label(window,text=text).pack()
    window.after(5000,idle_or_not)
def update_moves():
    global total_mouse_moves,total_keyboard_clicks
    total_mouse_moves=mouse.get_total_mouse_moves()
    total_keyboard_clicks=get_total_keyboard_clicks()
    window.after(6000,update_moves)
def show_log_info():
    update_moves()
    mouse_text=f"Total number of mouse moves are {total_mouse_moves}"
    Label(window,text=mouse_text).pack()
    keyboard_text=f"Total number of keyboard clicks are {total_keyboard_clicks}"
    Label(window,text=keyboard_text).pack()
window.after(2000,idle_or_not)
window.after(3000  ,update_moves)
button=Button(window,text="Get logging info",command=show_log_info)
button.pack()
positions=set()
def get_mouse_pos():
    positions.add(window.winfo_pointerxy())
    mouse.write_to_file(positions)
    window.after(100, get_mouse_pos)
get_mouse_pos()
listen_to_keyboard()
window.mainloop()


