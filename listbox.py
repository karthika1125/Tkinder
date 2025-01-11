from tkinter import*
from tkinter import ttk
root=Tk()
root.title("Listbox")
listbox=Listbox(root,width=45,height=15,bd=5,fg="red",bg="black")
listbox.pack(pady=20)
listbox.insert(0,"c")
listbox.insert(1,"c++")
listbox.insert(2,"java")
listbox.insert(3,"python")
root.geometry("500x600")
root,mainloop()