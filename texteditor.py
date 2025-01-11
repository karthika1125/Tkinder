from tkinter import*
root=Tk()
root.title("Text editor")
def callback():
    text=TextEditor.get(0.1,END)
TextEditor=Text(root,width=43,height=10,fg="white",bd=3,bg="black")
TextEditor.pack()
btn=Button(root,text="Display Text",command=callback)
btn.pack(pady=12)
root.geometry("300x500")
root.mainloop()    