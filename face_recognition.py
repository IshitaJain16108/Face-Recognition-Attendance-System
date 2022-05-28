from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
import cv2
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Detect faces')

        img1=Image.open(r'images\bg.png')
        img1=img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img1)
        
        lbl_img1=Label(self.root,image=self.photoimg)
        lbl_img1.place(x=0,y=0)

        btn=Button(self.root,text="Recognize Face",command=self.face_recog,font=('arial',30,'bold'),width=16,bg='#f2d694',fg='black',cursor='hand2')
        btn.place(x=900,y=700,width=400,height=50)

    # Attendance
    def mark_attendance(self,i,j):
        with open("attendance.csv","r+",newline="\n") as f:
            myData=f.readlines()
            name_list=[]
            for line in myData:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list)) and ((j not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{j},Present,{d1},{dtString}")

    # Face Recognition
    def face_recog(self):
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=faceCascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=10)
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                id1=str(id)
                confidence=int(100*((1-predict/300)))

                conn=mysql.connector.connect(host='localhost',user='root',password='8295351575Ij@',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute("select Name from employee where ID_Proof="+id1)
                n=my_cursor.fetchone()

                my_cursor1=conn.cursor()
                my_cursor1.execute("select Department from employee where ID_Proof="+id1)
                d=my_cursor1.fetchone()

                if confidence>50:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    self.mark_attendance(n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
            #img1=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome to Face recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()

        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()