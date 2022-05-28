from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Train Images')

        img1=Image.open(r'images\C3.png')
        img1=img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img1)
        
        lbl_img1=Label(self.root,image=self.photoimg)
        lbl_img1.place(x=0,y=0)

        btn=Button(self.root,text="Train Data Set",command=self.train_classifier,font=('arial',30,'bold'),width=16,bg='#f2d694',fg='black',cursor='hand2')
        btn.place(x=200,y=300,width=400,height=50)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=50,y=450,width=600,height=200)

        img2=Image.open(r'images\img.png')
        img2=img2.resize((610,210),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img2)
        
        lbl_img2=Label(img_frame,image=self.photoimg1)
        lbl_img2.place(x=-10,y=-10)

    def train_classifier(self):
        dir=r"C:\Users\pc\OneDrive\Desktop\frs\data"
        path=[os.path.join(dir,file) for file in os.listdir(dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # train classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        messagebox.showinfo("Result","Training Dataset Completed")

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
