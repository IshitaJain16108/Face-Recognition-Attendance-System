from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Managament System')

        # Variables
        self.var_empid=StringVar()
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_degi=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

        image=Image.open(r'images\Capture1.png')
        image=image.resize((1550,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(image)
        
        lbl_bg=Label(self.root,image=self.photoimg)
        lbl_bg.place(x=-10,y=0)

        # Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=175,width=1510,height=580)

        # Upper Frame 
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1490,height=260)

        # Labels and Entries fields
        # Employee ID
        lbl_empid=Label(upper_frame,font=('arial',12,'bold'),text='Employee ID',bg='white')
        lbl_empid.grid(row=0,column=0,padx=2,pady=7,sticky=W)

        txt_empid=ttk.Entry(upper_frame,textvariable=self.var_empid,font=('arial',11,'bold'),width=22)
        txt_empid.grid(row=0,column=1,padx=2,pady=7)

        # Departemnt
        lbl_dep=Label(upper_frame, text='Department',font=('arial',12,'bold'),bg='white')
        lbl_dep.grid(row=0,column=2,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',10,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','PR','Sales','Finance','Operations','Purchase')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Name
        lbl_Name=Label(upper_frame,font=('arial',12,'bold'),text='Name',bg='white')
        lbl_Name.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,font=('arial',11,'bold'),width=22)
        txt_name.grid(row=0,column=5,padx=2,pady=7)

        # lbl_designation
        lbl_Designation=Label(upper_frame,font=('arial',12,'bold'),text='Designation',bg='white')
        lbl_Designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_degi,font=('arial',11,'bold'),width=22)
        txt_Designation.grid(row=1,column=1,padx=2,pady=7)

        # Email
        lbl_email=Label(upper_frame,font=('arial',12,'bold'),text='Email',bg='white')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,font=('arial',11,'bold'),width=22)
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        # Address
        lbl_Address=Label(upper_frame,font=('arial',12,'bold'),text='Address',bg='white')
        lbl_Address.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,font=('arial',11,'bold'),width=22)
        txt_Address.grid(row=1,column=5,padx=2,pady=7)

        # Married
        lbl_married_status=Label(upper_frame,text='Married Status',font=('arial',12,'bold'),bg='white')
        lbl_married_status.grid(row=2,column=0,padx=2,sticky=W)

        combo_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',10,'bold'),width=17,state='readonly')
        combo_txt_married['value']=('Select Marital Status','Married','Unmarried')
        combo_txt_married.current(0)
        combo_txt_married.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # DOB
        lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text='Date of Birth',bg='white')
        lbl_dob.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,font=('arial',11,'bold'),width=22)
        txt_dob.grid(row=2,column=3,padx=2,pady=7)

        # DOJ
        lbl_doj=Label(upper_frame,font=('arial',12,'bold'),text='Date of Joining',bg='white')
        lbl_doj.grid(row=2,column=4,padx=4,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,font=('arial',11,'bold'),width=22)
        txt_doj.grid(row=2,column=5,padx=2,pady=7)

        # Id Proof
        combo_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('arial',10,'bold'),width=17,state='readonly')
        combo_txt_proof['value']=('Select ID Proof','Pan Card','Adhaar Card','Driving licence')
        combo_txt_proof.current(0)
        combo_txt_proof.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,font=('arial',11,'bold'),width=22)
        txt_proof.grid(row=3,column=1,padx=2,pady=7)

        # Gender
        lbl_gender=Label(upper_frame, text='Gender',font=('arial',12,'bold'),bg='white')
        lbl_gender.grid(row=3,column=2,padx=2,sticky=W)

        combo_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',10,'bold'),width=17,state='readonly')
        combo_txt_gender['value']=('Select Gender','Male','Female','Other')
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=3,column=3,padx=2,pady=10,sticky=W)

        # Phone 
        lbl_phone=Label(upper_frame,font=('arial',12,'bold'),text='Phone Number',bg='white')
        lbl_phone.grid(row=3,column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,font=('arial',11,'bold'),width=22)
        txt_phone.grid(row=3,column=5,padx=2,pady=7)

        # Country
        lbl_country=Label(upper_frame,font=('arial',12,'bold'),text='Country',bg='white')
        lbl_country.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,font=('arial',11,'bold'),width=22)
        txt_country.grid(row=4,column=1,padx=2,pady=7)

        #CTC
        lbl_ctc=Label(upper_frame,font=('arial',12,'bold'),text='Salary (CTC)',bg='white')
        lbl_ctc.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,font=('arial',11,'bold'),width=22)
        txt_ctc.grid(row=4,column=3,padx=2,pady=7)

        # Image
        employee=Image.open(r'images\employee.png')
        employee=employee.resize((220,220),Image.ANTIALIAS)
        self.emp=ImageTk.PhotoImage(employee)

        self.employee=Label(upper_frame,image=self.emp,bg='white')
        self.employee.place(x=1025,y=0,width=200,height=200)

        # Radio Buttons
        self.var_radio1=StringVar()
        frame1=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        frame1.place(x=1000,y=205,width=270,height=25)

        radiobtn1=ttk.Radiobutton(frame1,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.place(x=0,y=0,width=145,height=25)

        radiobtn2=ttk.Radiobutton(frame1,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.place(x=145,y=0,width=125,height=25)

        # Button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1290,y=15,width=170,height=200)

        btn_add=Button(button_frame,command=self.add_data,text="Save",font=('arial',12,'bold'),width=16,bg='red',fg='white',cursor='hand2')
        btn_add.grid(row=0,column=0)

        btn_update=Button(button_frame,command=self.update_data,text="Update",font=('arial',12,'bold'),width=16,bg='red',fg='white',cursor='hand2')
        btn_update.grid(row=1,column=0)

        btn_delete=Button(button_frame,command=self.delete_data,text="Delete",font=('arial',12,'bold'),width=16,bg='red',fg='white',cursor='hand2')
        btn_delete.grid(row=2,column=0)

        btn_clear=Button(button_frame,command=self.clear_data,text="Clear",font=('arial',12,'bold'),width=16,bg='red',fg='white',cursor='hand2')
        btn_clear.grid(row=3,column=0)

        btn_take_photo=Button(button_frame,command=self.generate_dataset,text="Take Photo Sample",font=('arial',12,'bold'),width=16,bg='red',fg='white',cursor='hand2')
        btn_take_photo.grid(row=4,column=0)

        btn_update_photo=Button(button_frame,text="Update Photo Sample",command=self.generate_dataset,font=('arial',12,'bold'),width=16,bg='red',fg='white',cursor='hand2')
        btn_update_photo.grid(row=5,column=0)

        # Lower Frame 
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1490,height=300)

        # Search
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=5,y=0,width=1475,height=60)

        search_by=Label(search_frame,text='Search By:',font=('arial',11,'bold'),bg='blue',fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=('Select Option','Phone_No','ID_Proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="Search",font=("arial",11,"bold"),width=14,bg="red",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,text="Show All",font=("arial",11,"bold"),width=14,bg="red",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)

        # ================ Employee Table ================
        # Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=65,width=1475,height=200)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.table=ttk.Treeview(table_frame,column=("id","dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        self.table.heading('id',text='Employee_Id')
        self.table.heading('dep',text='Department')
        self.table.heading('name',text='Name')
        self.table.heading('degi',text='Designation')
        self.table.heading('email',text='Email')
        self.table.heading('address',text='Address')
        self.table.heading('married',text='Marital Status')
        self.table.heading('dob',text='Date of Birth')
        self.table.heading('doj',text='Date of Joining')
        self.table.heading('idproofcomb',text='ID Type')
        self.table.heading('idproof',text='ID Proof')
        self.table.heading('gender',text='Gender')
        self.table.heading('phone',text='Phone Number')
        self.table.heading('country',text='Country')
        self.table.heading('salary',text='Salary')
        self.table.heading('photo',text='Photo Status')

        self.table['show']='headings'

        self.table.column("id",width=100)
        self.table.column("dep",width=100)
        self.table.column("name",width=100)
        self.table.column("degi",width=100)
        self.table.column("email",width=100)
        self.table.column("address",width=100)
        self.table.column("married",width=100)
        self.table.column("dob",width=100)
        self.table.column("doj",width=100)
        self.table.column("idproofcomb",width=100)
        self.table.column("idproof",width=100)
        self.table.column("gender",width=100)
        self.table.column("phone",width=100)
        self.table.column("country",width=100)
        self.table.column("salary",width=100)
        self.table.column("photo",width=100)

        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

# =========================Functions========================
    # Add data
    def add_data(self):
        if self.var_dep.get()=="" or self.var_dep.get()=="" or self.var_name.get()=="" or self.var_degi.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_married.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_idproofcomb.get()=="" or self.var_idproof.get()=="" or self.var_gender.get()=="" or self.var_phone.get()=="" or self.var_country.get()=="" or self.var_salary.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='8295351575Ij@',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_empid.get(),self.var_dep.get(),self.var_name.get(),self.var_degi.get(),self.var_email.get(),self.var_address.get(),self.var_married.get(),self.var_dob.get(),self.var_doj.get(),self.var_idproofcomb.get(),self.var_idproof.get(),self.var_gender.get(),self.var_phone.get(),self.var_country.get(),self.var_salary.get(),self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    
    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='8295351575Ij@',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.table.focus()
        content=self.table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_dep.set(data[1])
        self.var_name.set(data[2])
        self.var_degi.set(data[3])
        self.var_email.set(data[4])
        self.var_address.set(data[5])
        self.var_married.set(data[6])
        self.var_dob.set(data[7])
        self.var_doj.set(data[8])
        self.var_idproofcomb.set(data[9])
        self.var_idproof.set(data[10])
        self.var_gender.set(data[11])
        self.var_phone.set(data[12])
        self.var_country.set(data[13])
        self.var_salary.set(data[14])
        self.var_radio1.set(data[15])

    # Update
    def update_data(self):
        if self.var_dep.get()=="" or self.var_dep.get()=="" or self.var_name.get()=="" or self.var_degi.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_married.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_idproofcomb.get()=="" or self.var_idproof.get()=="" or self.var_gender.get()=="" or self.var_phone.get()=="" or self.var_country.get()=="" or self.var_salary.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update employee data')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='8295351575Ij@',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee set Employee_Id=%s,Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Marital_Status=%s,Date_of_Birth=%s,Date_of_Joining=%s,ID_Type=%s,Gender=%s,Phone_No=%s,Country=%s,Salary=%s,Photo_Status=%s where ID_Proof=%s',(self.var_empid.get(),self.var_dep.get(),self.var_name.get(),self.var_degi.get(),self.var_email.get(),self.var_address.get(),self.var_married.get(),self.var_dob.get(),self.var_doj.get(),self.var_idproofcomb.get(),self.var_gender.get(),self.var_phone.get(),self.var_country.get(),self.var_salary.get(),self.var_radio1.get(),self.var_idproof.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee Successfully Updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # Delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure to delete previous data')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='8295351575Ij@',database='mydata')
                    my_cursor=conn.cursor()
                    sql='delete from employee where ID_Proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # Reset
    def clear_data(self):
        self.var_dep.set("")
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_degi.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Select Marital Status")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("Select Gender")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")
        self.var_radio1.set("")

    # Search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='8295351575Ij@',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.table.delete(*self.table.get_children())
                    for i in rows:
                        self.table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # Take a photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="" or self.var_dep.get()=="" or self.var_name.get()=="" or self.var_degi.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_married.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_idproofcomb.get()=="" or self.var_idproof.get()=="" or self.var_gender.get()=="" or self.var_phone.get()=="" or self.var_country.get()=="" or self.var_salary.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='8295351575Ij@',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                
                my_cursor.execute('update employee set Employee_Id=%s,Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Marital_Status=%s,Date_of_Birth=%s,Date_of_Joining=%s,ID_Type=%s,Gender=%s,Phone_No=%s,Country=%s,Salary=%s,Photo_Status=%s where ID_Proof=%s',(self.var_dep.get(),self.var_dep.get(),self.var_name.get(),self.var_degi.get(),self.var_email.get(),self.var_address.get(),self.var_married.get(),self.var_dob.get(),self.var_doj.get(),self.var_idproofcomb.get(),self.var_gender.get(),self.var_phone.get(),self.var_country.get(),self.var_salary.get(),self.var_radio1.get(),self.var_idproof.get()))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()

                # Load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1 
                    #face=cv2.resize(face_cropped(myframe),(0,0),fx=0.1,fy=0.1)
                    face=cv2.cvtColor(myframe,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(433,320),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset Generation Completed")
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()