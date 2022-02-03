
"""import tkinter
import login
window=tkinter.Tk()
window.geometry("800x200")
top_frame=tkinter.Frame(window).pack()
tkinter.Label(window,top_frame, text="Username").pack()
user_entry=tkinter.Entry(window)
user_entry.pack()
tkinter.Label(window, text="Password").pack()
pass_entry=tkinter.Entry(window)
pass_entry.pack()
def clicked():
    user_name=user_entry.get()
    password=pass_entry.get()
    if login.does_user_exist(user_name): 
         
        if login.is_password_valid(user_name, password):
            pass
        else:
            tkinter.Label(window,text="Passworrd invalid").pack()
    else:
        tkinter.Label(window,text="USer does not exist").pack()
tkinter.Button(window, text="Enter",command=clicked).pack()      
window.mainloop()"""
import tkinter as tk
import login
from tkinter import ttk
from tkinter.messagebox import showinfo
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login page')
        self.geometry('800x200')

        self.label1 = ttk.Label(self, text='Username')
        self.label1.pack()

        self.entry1 = ttk.Entry(self)
        self.entry1.pack()

        self.label2=ttk.Label(self, text="Password")
        self.label2.pack()

        self.entry2= ttk.Entry(self)
        self.entry2.pack()

        self.button = ttk.Button(self, text='Enter')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        user_name=self.entry1.get()
        password=self.entry2.get()
        if login.does_user_exist(user_name):

         
            if login.is_password_valid(user_name, password):
                pass
            else:
                showinfo(title='Information',
                    message='Password invalid')
        else:
            showinfo(title='Information',
                    message='User does not exit')
   


if __name__ == "__main__":
    app = App()
    app.mainloop()