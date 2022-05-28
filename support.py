from tkinter import*
from PIL import Image,ImageTk


class Support:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Support System')

        image=Image.open(r'images\help.jpg')
        image=image.resize((1550,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(image)
        
        lbl_bg=Label(self.root,image=self.photoimg)
        lbl_bg.place(x=-10,y=0)

        help_label=Label(lbl_bg,text="Email: ishitajain0667@gmail.com",font=('arial',15,'bold'),fg='blue',bg='white')
        help_label.place(x=100,y=200)

if __name__=="__main__":
    root=Tk()
    obj=Support(root)
    root.mainloop()