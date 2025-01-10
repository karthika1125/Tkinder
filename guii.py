# from tkinter import*
# root=Tk()
# root.title("Welcome")
# x=Label(root,text="Welcome to my page",font=("Arial",18),fg='red')
# x.pack()
# x1=Label(root,text="username",font=("Garamond",14),fg="black")
# x1.place(x=10,y=50)
# e1=Entry(root,bg="grey",fg="black",bd=3)
# e1.place(x=90,y=50)
# x2=Label(root,text="password",font=("Garamond",14),fg="black")
# x2.place(x=10,y=100)
# e2=Entry(root,bg="grey",fg="black",bd=3)
# e2.place(x=90,y=100)
# def login():
#     print("your are log in")
# btn=Button(root,text="Log in",fg="blue",font=("Garamond",14),command=login)
# btn.place(x=130,y=130)
# root.geometry('300x200')
# root.mainloop()


                               #checkbutton
# from tkinter import*
# root=Tk()
# root.title("Welcome")
# w=Label(root,text="Gender",font=("Arial",14))
# w.pack()
# checkbox1=IntVar()
# checkbox2=IntVar()
# btn=Checkbutton(root,text="Maths",variable=checkbox1,onvalue=1,offvalue=0,height=3,width=12)
# btn2=Checkbutton(root,text="Chemistry",variable=checkbox2,onvalue=1,offvalue=0,height=3,width=12)
# btn.pack()
# btn2.pack()
# root.geometry("200x300")
# root.mainloop()


                               #Radiobutton
# from tkinter import*
# root=Tk()
# root.title("Welcome")
# v=StringVar(root,"1")
# rbtn=Radiobutton(root,text="Female",variable=v,value="1")
# rbtn.pack()
# rbtn1=Radiobutton(root,text="Male",variable=v,value="2")
# rbtn1.pack()
# root.geometry("200x300")
# root.mainloop()


                               #image


from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Welcome")


path = Image.open("C:/Users/HP/OneDrive/Desktop/python1/image.png")
image = path.resize((400, 400))  
photo = ImageTk.PhotoImage(image)


label_image = Label(root, image=photo)
label_image.pack()


root.geometry("300x200")  


label_image.image = photo


mainloop()

