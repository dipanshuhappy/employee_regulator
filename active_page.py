import tkinter 
import mouse
root=tkinter.Tk()
lbl = tkinter.Label(root, width=20)
lbl.pack()
positions=set()
def get_mouse_pos():
    positions.add(root.winfo_pointerxy())
    lbl.config(text='{}, {}'.format(*root.winfo_pointerxy()))
    mouse.write_to_file(positions)
    root.after(100, get_mouse_pos)
get_mouse_pos()
root.mainloop()