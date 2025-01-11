from tkinter import*
root=Tk()
root.title("Canvas")
c1=Canvas(root,bg="yellow",width=550,height=250)
c1.place(x=50,y=50)
rectangle=c1.create_rectangle(30,20,140,90,fill="light green")
poly=c1.create_line(120,150,60,200,50,80,fill="blue")
arc=c1.create_arc(200,400,60,20,fill="black")
oval=c1.create_oval(250,120,200,100,fill="red")

root.geometry("300x200")
root.mainloop()