import tkinter
window=tkinter.Tk()
window.geometry("800x200")
top_frame=tkinter.Frame(window).pack()
tkinter.Label(window, top_frame, text="Username").pack()
tkinter.Entry(window).pack()
tkinter.Label(window, text="Password").pack()
tkinter.Entry(window).pack()
window.mainloop()