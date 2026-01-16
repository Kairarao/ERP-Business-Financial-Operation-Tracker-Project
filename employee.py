from tkinter import*
import mysql.connector
from conn import *
from color_palette import *


class employeeClass:
    def __init__(self,root):
        self.root=root
        width = root.winfo_screenwidth()
        self.root.geometry(f"{width-280}x{610}+255+145")
        self.root.title("Inventory Management System")
        #self.root.config(bg="white")
        self.root.resizable(False,False)
        self.root.focus_force()
        self.frame = Frame(self.root)
        self.frame.pack(fill='both', expand=True)
        palette=Color_Palette()
        palette.apply_to_window(self.frame)


        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="", database="ims_p25")
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred due to {ex}")
        #------------ all variables --------------
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()

        #---------- Search Frame -------------
        SearchFrame=LabelFrame(self.frame,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief="ridge",bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        palette.apply_to_slider(SearchFrame,self.var_searchby)

        #------------ options ----------------
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify="center",font=("goudy old style",15), style="custom.TCombobox")
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)


        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=200,y=10)
        btn_search=Button(SearchFrame,command=self.search,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2")
        btn_search.place(x=410,y=9,width=150,height=30)

        #-------------- title ---------------
        title=Label(self.frame,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white")
        title.place(x=50,y=100,width=1000)

        #-------------- content ---------------
        #---------- row 1 ----------------
        lbl_empid=Label(self.frame,text="Emp ID",font=("goudy old style",15),bg="white")
        lbl_empid.place(x=50,y=150)
        lbl_gender=Label(self.frame,text="Gender",font=("goudy old style",15),bg="white")
        lbl_gender.place(x=350,y=150)
        lbl_contact=(Label(self.frame,text="Contact",font=("goudy old style",15),bg="white"))
        lbl_contact.place(x=750,y=150)
        palette.apply_to_label(lbl_empid)
        palette.apply_to_label(lbl_gender)
        palette.apply_to_label(lbl_contact)
        txt_empid=Entry(self.frame,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow")
        txt_empid.place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.frame,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify="center",font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.frame,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow")
        txt_contact.place(x=850,y=150,width=180)
        palette.apply_to_entry(txt_empid)
        palette.apply_to_entry(txt_contact)
        palette.apply_to_entry(txt_search)
        #---------- row 2 ----------------
        lbl_name=Label(self.frame,text="Name",font=("goudy old style",15),bg="white")
        lbl_name.place(x=50,y=190)
        lbl_dob=Label(self.frame,text="D.O.B.",font=("goudy old style",15),bg="white")
        lbl_dob.place(x=350,y=190)
        lbl_doj=Label(self.frame,text="D.O.J.",font=("goudy old style",15),bg="white")
        lbl_doj.place(x=750,y=190)

        txt_name=Entry(self.frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow")
        txt_name.place(x=150,y=190,width=180)
        txt_dob=Entry(self.frame,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow")
        txt_dob.place(x=500,y=190,width=180)
        txt_doj=Entry(self.frame,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow")
        txt_doj.place(x=850,y=190,width=180)

        #---------- row 3 ----------------
        lbl_email=Label(self.frame,text="Email",font=("goudy old style",15),bg="white")
        lbl_email.place(x=50,y=230)
        lbl_pass=Label(self.frame,text="Password",font=("goudy old style",15),bg="white")
        lbl_pass.place(x=350,y=230)
        lbl_utype=Label(self.frame,text="User Type",font=("goudy old style",15),bg="white")
        lbl_utype.place(x=750,y=230)

        txt_email=Entry(self.frame,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow")
        txt_email.place(x=150,y=230,width=180)
        txt_pass=Entry(self.frame,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow")
        txt_pass.place(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.frame,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify="center",font=("goudy old style",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)
        
        #---------- row 4 ----------------
        lbl_address=Label(self.frame,text="Address",font=("goudy old style",15),bg="white")
        lbl_address.place(x=50,y=270)
        lbl_salary=Label(self.frame,text="Salary",font=("goudy old style",15),bg="white")
        lbl_salary.place(x=500,y=270)

        self.txt_address=Text(self.frame,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.frame,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow")
        txt_salary.place(x=600,y=270,width=180)
        
        #-------------- buttons -----------------
        btn_add=Button(self.frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2")
        btn_add.place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2")
        btn_update.place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2")
        btn_delete.place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2")
        btn_clear.place(x=860,y=305,width=110,height=28)

        #------------ employee details -------------
        emp_frame=Frame(self.frame,bd=3,relief="ridge")
        emp_frame.place(x=0,y=350,relwidth=1,height=300)

        scrolly=Scrollbar(emp_frame,orient="vertical")
        scrollx=Scrollbar(emp_frame,orient="horizontal")
        
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side="bottom",fill="x")
        scrolly.pack(side="right",fill="y")
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable["show"]="headings"
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        
        self.EmployeeTable.pack(fill="both",expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        palette.apply_to_treeview(self.EmployeeTable)
        # Assuming palette = Color_Palette() or imported palette instance is available

        # Labels
        palette.apply_to_label(lbl_empid)
        palette.apply_to_label(lbl_gender)
        palette.apply_to_label(lbl_contact)
        palette.apply_to_label(lbl_name)
        palette.apply_to_label(lbl_dob)
        palette.apply_to_label(lbl_doj)
        palette.apply_to_label(lbl_email)
        palette.apply_to_label(lbl_pass)
        palette.apply_to_label(lbl_utype)
        palette.apply_to_label(lbl_address)
        palette.apply_to_label(lbl_salary)
        palette.apply_to_label(title)

        # Entries
        palette.apply_to_entry(txt_search)
        palette.apply_to_entry(txt_empid)
        palette.apply_to_entry(txt_contact)
        palette.apply_to_entry(txt_name)
        palette.apply_to_entry(txt_dob)
        palette.apply_to_entry(txt_doj)
        palette.apply_to_entry(txt_email)
        palette.apply_to_entry(txt_pass)
        palette.apply_to_entry(txt_salary)

        # Comboboxes


        # Text widget
        palette.apply_to_text(self.txt_address)

        # Buttons
        palette.apply_to_button(btn_search)
        palette.apply_to_button(btn_add)
        palette.apply_to_button(btn_update)
        palette.apply_to_button(btn_delete)
        palette.apply_to_button(btn_clear)

        # Treeview
        palette.apply_to_treeview(self.EmployeeTable)

        # Scrollbars (if you want to apply slider style)
        palette.apply_to_slider(scrolly)
        palette.apply_to_slider(scrollx)

        self.show()
#-----------------------------------------------------------------------------------------------------
    def add(self):
        
        cur=self.con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where emp_id=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID is already assigned",parent=self.root)
                else:
                    cur.execute("insert into employee(emp_id,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                    ))
                    self.con.commit()
                    messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):

        cur=self.con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',"end",values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):

        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        if row:
        # set variables

            self.var_emp_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_contact.set(row[4])
            self.var_dob.set(row[5])
            self.var_doj.set(row[6])
            self.var_pass.set(row[7])
            self.var_utype.set(row[8])
            self.txt_address.delete('1.0',END)
            self.txt_address.insert(END,row[9])
            self.var_salary.set(row[10])

    def update(self):

        cur=self.con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where emp_id=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    query = """update employee set name=%s, email=%s, gender=%s, contact=%s, dob=%s, doj=%s, pass=%s, utype=%s, address=%s, salary=%s where emp_id=%s"""
                    values = (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END).strip(),
                        self.var_salary.get(),
                        self.var_emp_id.get(),
                    )
                    cur.execute(query, values)
                    self.con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def delete(self):

        cur=self.con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where emp_id=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where emp_id=%s",(self.var_emp_id.get(),))
                        self.con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()

    def search(self):

        cur=self.con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',"end",values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()