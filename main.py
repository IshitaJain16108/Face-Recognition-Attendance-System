from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from time import strftime
from employee import Employee
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from support import Support

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")

        image=Image.open(r'images\Capture.png')
        image=image.resize((1550,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(image)
        
        lbl_bg=Label(self.root,image=self.photoimg)
        lbl_bg.place(x=-10,y=0)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_bg,font=('arial',15,'bold'),bg='#f2d694')
        lbl.place(x=20,y=750)
        time()
        
        img1=Image.open(r'images\employee.png')
        img1=img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1=Button(lbl_bg,image=self.photoimg1,command=self.employee_details,cursor='hand2',borderwidth=5)
        b1.place(x=200,y=150)

        b1_1=Button(lbl_bg,text="Employee Details",command=self.employee_details,cursor='hand2',font=("times new roman",10,"bold"),fg='black',bg='#f2d694',borderwidth=5)
        b1_1.place(x=200,y=350,width=210)

        img2=Image.open(r'images\face.jpg')
        img2=img2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(lbl_bg,image=self.photoimg2,cursor='hand2',command=self.face_recognition,borderwidth=5)
        b2.place(x=650,y=150)

        b2_1=Button(lbl_bg,text="Face Detector",cursor='hand2',command=self.face_recognition,font=("times new roman",10,"bold"),fg='black',bg='#f2d694',borderwidth=5)
        b2_1.place(x=650,y=350,width=210)

        img3=Image.open(r'images\attendance.jpg')
        img3=img3.resize((200,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(lbl_bg,image=self.photoimg3,cursor='hand2',command=self.attendance,borderwidth=5)
        b3.place(x=1100,y=150)

        b3_1=Button(lbl_bg,text="Attendance",cursor='hand2',command=self.attendance,font=("times new roman",10,"bold"),fg='black',bg='#f2d694',borderwidth=5)
        b3_1.place(x=1100,y=350,width=210)

        img4=Image.open(r'images\train.png')
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(lbl_bg,image=self.photoimg4,cursor='hand2',command=self.train_data,borderwidth=5)
        b4.place(x=200,y=450)

        b4_1=Button(lbl_bg,text="Train Face",cursor='hand2',command=self.train_data,font=("times new roman",10,"bold"),fg='black',bg='#f2d694',borderwidth=5)
        b4_1.place(x=200,y=650,width=212)

        img5=Image.open(r'images\photo.png')
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(lbl_bg,image=self.photoimg5,cursor='hand2',borderwidth=5,command=self.open_img)
        b5.place(x=650,y=450)

        b5_1=Button(lbl_bg,text="Photos",cursor='hand2',command=self.open_img,font=("times new roman",10,"bold"),fg='black',bg='#f2d694',borderwidth=5)
        b5_1.place(x=650,y=650,width=210)

        img6=Image.open(r'images\exit.jpg')
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(lbl_bg,image=self.photoimg6,cursor='hand2',command=self.iExit,borderwidth=5)
        b6.place(x=1100,y=450)

        b6_1=Button(lbl_bg,text="Exit",cursor='hand2',command=self.iExit,font=("times new roman",10,"bold"),fg='black',bg='#f2d694',borderwidth=5)
        b6_1.place(x=1100,y=650,width=210)

        b7=Button(lbl_bg,text="Help Desk",command=self.support,cursor='hand2',font=("times new roman",10,"bold"),bg="#f2d694")
        b7.place(x=1450,y=750)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure you want to exit this project")
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    # Function Buttons
    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def support(self):
        self.new_window=Toplevel(self.root)
        self.app=Support(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
