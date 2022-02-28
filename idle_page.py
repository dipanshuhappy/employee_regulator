from logger import listen_to_keyboard,get_total_keyboard_clicks
import mouse
import tkinter as tk
from tkinter.ttk import *

class IdlePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.info_label=Label(self, text="Keylogger is running")
        self.info_label.pack()
        self.button=Button(self,text="Get logging info",command=self.show_log_info)
        self.button.pack()
        self.positions=set()
        self.start_logging()
        self.total_mouse_moves=0
        self.total_keyboard_clicks=0
    def start_logging(self):
        self.after(2000,self.idle_or_not)
        self.after(3000  ,self.update_moves)
        self.get_mouse_pos()
        listen_to_keyboard()
    def idle_or_not(self):
        new_keyboard=get_total_keyboard_clicks()
        print(f'old_keyboard_click:{self.total_keyboard_clicks} and  new {new_keyboard}')
        new_mouse=mouse.get_total_mouse_moves()
        print(f'total mouse :{self.total_mouse_moves} and new {new_mouse}')
        idle=self.total_keyboard_clicks==new_keyboard and self.total_mouse_moves==new_mouse
        print(idle)
        text=f'You are idle {idle}'
        Label(self,text=text).pack()
        self.after(5000,self.idle_or_not)
    def update_moves(self):
        self.total_mouse_moves=mouse.get_total_mouse_moves()
        self.total_keyboard_clicks=get_total_keyboard_clicks()
        self.after(6000,self.update_moves)
    def show_log_info(self):
        self.update_moves()
        mouse_text=f"Total number of mouse moves are {self.total_mouse_moves}"
        Label(self,text=mouse_text).pack()
        keyboard_text=f"Total number of keyboard clicks are {self.total_keyboard_clicks}"
        Label(self,text=keyboard_text).pack()
    def get_mouse_pos(self):
        self.positions.add(self.winfo_pointerxy())
        mouse.write_to_file(self.positions)
        self.after(100, self.get_mouse_pos)
IdlePage().mainloop()