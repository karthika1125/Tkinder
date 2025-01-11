from tkinter import*
root=Tk()
root.title("Frame")
bottam=Frame(root,bd=3,bg="green",width=120,height=600,)

bottam.place(x=50,y=50)

b1=Frame(root,bd=3,bg="blue",width=120,height=600)
b1.place(x=100,y=50)
b2=Frame(root,bd=3,bg="purple",width=120,height=600)
b2.place(x=150,y=50)
b3=Frame(root,bd=3,bg="red",height=120,width=600)
b3.place(x=200,y=50)
b4=Frame(root,bd=3,bg="black",height=120,width=600)
b4.place(x=200,y=100)
b5=Frame(root,bd=3,bg="yellow",height=120,width=600)
b5.place(x=200,y=150)
b6=Frame(root,bd=3,bg="green",width=120,height=600,)

b6.place(x=400,y=50)

b7=Frame(root,bd=3,bg="blue",width=120,height=600)
b7.place(x=450,y=50)
b8=Frame(root,bd=3,bg="purple",width=120,height=600)
b8.place(x=500,y=50)
b9=Frame(root,bd=3,bg="red",height=120,width=600)
b9.place(x=500,y=200)
b10=Frame(root,bd=3,bg="black",height=120,width=600)
b10.place(x=500,y=250)
b11=Frame(root,bd=3,bg="yellow",height=120,width=600)
b11.place(x=500,y=350)

root.geometry("300x200")
root.mainloop()
