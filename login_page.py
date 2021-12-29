from os import terminal_size
import tkinter
import login
window=tkinter.Tk()
window.geometry("800x200")
top_frame=tkinter.Frame(window).pack()
tkinter.Label(window, top_frame, text="Username").pack()
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
window.mainloop()


