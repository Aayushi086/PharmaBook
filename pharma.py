from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        #========addmed variable===============
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()

        #======================main variable======================
        self.ref_var=StringVar
        self.cmpName_var=StringVar()

        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open(r"C:\Users\aayus\Downloads\pharma\pharmacy_logo.png")
        img1=img1.resize((80,80),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)
        
        #===============DataFrame============
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=("ariel",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        #===========ButtonsFrame===============
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        #=========MainButton=========
        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,text="Update",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDelMed=Button(ButtonFrame,text="DELETE",command=self.delete,font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnDelMed.grid(row=0,column=2)

        btnRestMed=Button(ButtonFrame,text="RESET",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnRestMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,text="EXIT",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)


        #=======SearchBy==========
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        #variable
        self.searc_var=StringVar()

        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.searc_var,width=12,font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)

        searchButton=Button(ButtonFrame,command=self.searc_var,text="SEARCH",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        searchButton.grid(row=0,column=8)

        showAll=Button(ButtonFrame,command=self.fetch_data,text="Show All",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)


        #============Lable AND Entry=====================
        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2,pady=6)
        lblrefno.grid(row=0,column=0,sticky=W)

    
        conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()

        lblrefno=Label(DataFrameLeft,font=("ariel",12,"bold"),text="Reference No",padx=2, pady=6)
        lblrefno.grid(row=0,column=0,sticky=W)

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,state="readonly",font=("arial",12,"bold"),width=27)
        ref_combo['values']=row
        ref_combo.grid(row=0,column=1)
        #ref_combo.current(0)
       

        lblCmpName=Label(DataFrameLeft, font=("arial", 12, "bold"), text=" Company Name", padx=2,pady=6)
        lblCmpName.grid(row=1,column=0, sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29) 
        txtCmpName.grid(row=1,column=1)

        lblTypeofMedicine=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Type Of Medicine", padx=2, pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)


        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var, state="readonly",font=("arial", 12, "bold"), width=27) 
        comTypeofMedicine['value']=("Tablet", "Liquid", "Capsules", "Topical Medicines", "Orops", "Inhales", "Injection")
        #comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)


        #=============AddMedicine=======================
        
        lblMedicineName=Label (DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name", padx=2, pady=6) 
        lblMedicineName.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select medName from pharma")

        

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,state="readonly", font=("arial", 12, "bold"), width=27)
        comMedicineName['value']=("nice", "novel")
        #comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)

        lblLotNo=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot No",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var, font=("arial", 13, "bold"), bg="white", bd=2, relief= RIDGE, width=29) 
        txtLotNo.grid(row=4,column=1)

        lblissueDate=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate =Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2,relief=RIDGE, width=29) 
        txtIssueDate.grid(row=5,column=1)

        lblExDate =Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6) 
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate= Entry(DataFrameLeft,textvariable=self.expdate_var, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29) 
        txtExDate.grid(row=6,column=1)


        lbluses= Label (DataFrameLeft, font=("arial", 12, "bold"), text="Uses:", padx=2, pady=4)
        lbluses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29) 
        txtUses.grid(row=7,column=1)

        lblSideEffect= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W) 
        txtSideEffect= Entry (DataFrameLeft,textvariable=self.sideEffect_var, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtSideEffect.grid(row=8,column=1)

        lb1Precwarning=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Prec&Warning:",padx=15)
        lb1Precwarning.grid(row=0,column=2,sticky=W) 
        txtPrecwarning= Entry(DataFrameLeft,textvariable=self.warning_var, font=("arial", 12, "bold"), bg="white",bd=2, relief=RIDGE, width=29) 
        txtPrecwarning.grid(row=0,column=3)

        lblDosage =Label (DataFrameLeft, font=("arial", 12, "bold"), text="Dosage:",padx=15,pady=6) 
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var, font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29) 
        txtDosage.grid(row=1,column=3)

        lblPrice =Label(DataFrameLeft, font=("arial", 12, "bold"), text="Tablets Price:", padx=15, pady=6) 
        lblPrice.grid(row=2,column=2, sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var, font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE,width=29) 
        txtPrice.grid(row=2,column=3)

        lblProduct =Label(DataFrameLeft, font=("arial", 12, "bold"), text="Product QT:", padx=15, pady=6) 
        lblProduct.grid(row=2,column=2, sticky=W)
        txtProduct=Entry(DataFrameLeft,textvariable=self.product_var, font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE,width=29) 
        txtProduct.grid(row=2,column=3)

        #=======================Images======================
        lblhome=Label(DataFrameLeft,font=("arial",15,"bold"),text="Bringing Wellness To Your Doorstep",padx=2,pady=5,bg="white",fg="red",width=30)
        lblhome.place(x=420,y=130)

        img2=Image.open(r"C:\Users\aayus\Downloads\pharma\Healthcare_pharmacist.jpeg")
        img2=img2.resize((300,150),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=600,y=320)



        #============dateFrameRight================
        # lblhome=Label(DataFrameLeft,font=("arial",15,"bold"),texts="")
        img3=Image.open(r"C:\Users\aayus\Downloads\pharma\pharmacy2.jpg")
        img3=img3.resize((200,75),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=960,y=160)

        img4=Image.open(r"C:\Users\aayus\Downloads\pharma\medicine1.jpg")
        img4=img4.resize((200,75),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1160,y=160)

        img5=Image.open(r"C:\Users\aayus\Downloads\pharma\medicine2.jpg")
        img5=img5.resize((200,145),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=1270,y=160)

        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference no.")
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",15,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtrefno.place(x=135,y=80)

        lblmedname=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine name")
        lblmedname.place(x=0,y=110)
        txtmedname=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",15,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtmedname.place(x=135,y=110)


        #============================side Frame================================

        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)


        #==========================medicine and buttons===================

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddmed=Button(down_frame,text="ADD",font=("arial",12,"bold"),bg="lime",fg="white",width=12,pady=2)
        btnAddmed.grid(row=0,column=0)

        btnUpdateMed=Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("arial",12,"bold"),bg="purple",fg="white",width=12,pady=2)
        btnUpdateMed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",12,"bold"),bg="red",fg="white",width=12,pady=2)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",12,"bold"),bg="orange",fg="white",width=12,pady=2)
        btnClearmed.grid(row=3,column=0)


        #===========================Frame Details================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=590,width=1530,height=210)

        #=============================Main table and scroll bar======================
        Table_frame=Frame(Framedetails,bd=15,relief=RIDGE)
        Table_frame.place(x=0,y=1,width=1460,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("ref","medname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("medname",text="Company name")
        self.pharmacy_table.heading("type",text="Type of medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet name")
        self.pharmacy_table.heading("lotno",text="Lot No.")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expiry Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product QTs")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("medname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)

        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

        #======================add medicine functionality declaration========================
    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,medName) values(%s,%s)",(
                 self.refMed_var.get(),
                 self.addmed_var.get()
        ))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor
        conn.close()
        messagebox.showinfo("success","Medicine Added")
        
    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #========================================MedGetCursor=======================
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.redMed_var.set(row[0])
        self.addmed_var.set(row[1])

    #===============

    def UpdateMed(self):
        if self.reference.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set medName=%s where Ref=%s",(
                self.AddMed_var.get(),
                self.refMed_var.get(),

            ))

            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.xhowinfo("Success","Medicine has been updated")
    
    
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
        my_cursor=conn.cursor()
        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()
    
    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")

    #==================main table================

    def add_data(self):
        if self.ref_var.get()=="" or self.lot_va.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.ref_var.get(),
                self.cmpName_var.get(),
                self.typeMed_var.get(), 
                self.medName_var.get(),

                self.lot_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(), 
                self.price_var.get(), 
                self.product_var.get()
            
            ) )  

            conn.commit()
            self.fetch_data()
            conn.close() 
            messagebox.showinfo("Success","Data has been inserted")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("","end",values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,ev=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0]),
        self.typeMed_var.set(row[2]),
        self.cmpName_var.set(row[1]), self.medName_var.set(row[3]), self.lot_var.set(row[4]), self.issuedate_var.set(row[5]), self.sideEffect_var.set(row[8]), self.warning_var.set(row[9]),
        self.expdate_var.set(row[6]), self.uses_var.set(row[7]),
        self.dosage_var.set(row[18]), self.price_var.set(row[11]),
        self.product_var.set(row[12])

    def Update(self):
          if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
          else:
                  
            conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set cmpName=%s,Type=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s,product=%s where refno=%s",(
                self.ref_var.get(),
                self.cmpName_var.get(),
                self.typeMed_var.get(), 
                self.medName_var.get(),

                self.lot_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(), 
                self.price_var.get(), 
                self.product_var.get()

            ))

            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success","Medicine has been updated")

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
        my_cursor=conn.cursor()
        sql="delete from pharmacy where refno=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Delete","Information deleted successfully")

    def reset(self):
        self.cmpName_var.set("")
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(""), 
        self.price_var.set(""), 
        self.product_var.set("")

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AayushiSingh@12345#",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where "+str(self.searchTxt_var.get())+"LIKE"+str(self.searchTxt_var.get()+"%"))
       
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()










        


            
            




















                                                                                

                                                                                





                                    
                                    

    
if __name__=="__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()