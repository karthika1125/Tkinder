from tkinter import*
from tkinter import ttk
root=Tk()
root.title("Paned Window")
pw=ttk.PanedWindow(root,orient=HORIZONTAL)
pw.pack(fill=BOTH,expand=True)
frame1=ttk.Frame(pw,relief=SUNKEN)
frame2=ttk.Frame(pw,relief=SUNKEN)
pw.add(frame1,weight=1)
pw.add(frame2,weight=3)
root.geometry("300x500")
root.mainloop()