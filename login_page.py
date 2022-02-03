
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
