from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from main import Face_Recognition_System

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        image=Image.open(r'images\Back.PNG')
        image=image.resize((1550,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(image)
        
        lbl_bg=Label(self.root,image=self.photoimg)
        lbl_bg.place(x=-10,y=0)

        frame=Frame(self.root,bg="black")
        frame.place(x=605,y=200,width=340,height=400)

        img1=Image.open(r"images\user.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbl_img1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lbl_img1.place(x=730,y=210,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg='white',bg='black')
        get_str.place(x=105,y=100)

        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg='white',bg='black')
        username.place(x=20,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.txtuser.place(x=20,y=180,width=300)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg='white',bg='black')
        password.place(x=20,y=210)

        self.txtpswrd=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")
        self.txtpswrd.place(x=20,y=240,width=300)        

        loginbtn=Button(frame,command=self.main_window,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,cursor="hand2",fg='white',bg='red',activeforeground='white',activebackground='red')
        loginbtn.place(x=110,y=280,width=120,height=35)

    def login(self):
        if self.txtuser.get()=="ishu" and self.txtpswrd.get()=="ish":
            messagebox.showinfo("Success","Welcome")
        elif self.txtuser.get()=="" or self.txtpswrd.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            messagebox.showerror("Invalid","Username and Password do not match")

    def main_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)
    
if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()