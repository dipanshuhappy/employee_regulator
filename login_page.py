
import tkinter as tk
import login
from tkinter import ttk
from tkinter.messagebox import showinfo
class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login page')
        self.geometry('800x200')

        self.username_label = ttk.Label(self, text='Username')
        self.username_label.pack()

        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        self.password_label=ttk.Label(self, text="Password")
        self.password_label.pack()

        self.password_entry= ttk.Entry(self,show='*')
        self.password_entry.pack()

        self.enter_button = ttk.Button(self, text='Enter')
        self.enter_button['command'] = self.button_clicked
        self.enter_button.pack()

        self.signup_button = ttk.Button(self, text='Sign Up')
        self.signup_button['command'] = self.signup_button_clicked
        self.signup_button.pack()
    def signup_button_clicked(self):
        user_name=self.username_entry.get()
        password=self.password_entry.get()
        self.handle_signup(user_name,password)
    def handle_signup(self,user_name,password):
        if login.does_user_exist(user_name):
            showinfo(title='Information',
                    message='User Exists')
        else:
            if (login.check_email(user_name)):
                login.add_user(user_name,password)
            else:
                showinfo(title='Information',
                    message='Invalid Email')
    def handle_login(self,user_name,password):
        if login.does_user_exist(user_name):
            if login.is_password_valid(user_name, password):
                pass
            else:
                showinfo(title='Information',
                    message='Password invalid')
        else:
            showinfo(title='Information',
                    message='User does not exit')
    def button_clicked(self):
        user_name=self.username_entry.get()
        password=self.password_entry.get()
        self.handle_login(user_name,password)

if __name__ == "__main__":
    LoginPage = LoginPage()
    LoginPage.mainloop()
