import csv
import re


from tkinter.ttk import Combobox
import mysql.connector
from tkinter import*
from tkinter.filedialog import Open,Directory
import os
# # tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "783151",database = "PythonDB")

# # # tạo đối tượng cursor
cur = myconn.cursor()

# dbs=cur.execute("CREATE TABLE if not exists Customers(first_name varchar(255) , "
#                 "last_name varchar(255) ,zipcode int(10)  , "
#                 "price_paid decimal(10,2),user_id int auto_increment primary key)")

# cur.execute("alter table Customers add (email varchar(255) ,"
#             "address_1 varchar(255) ,address_2 varchar(255),"
#             " city varchar(255) ,country varchar(255) ,"
#             "phone varchar(255) ,payment_method varchar(50) ,"
#             "discount_code varchar(255),state varchar(255))")
# sql = ("insert into Customers(first_name,last_name,zipcode,price_paid,user_id,email,address_1,"
#             "address_2,city,country,phone,payment_method,discount_code,state)" 
#             "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
# values=("Nguyen","Dat",123456,10,12345678,"cddd4f@yahoo.com","dong nai","dong nai","bien hoa","viet nam",
#         "02131313","visa","bd1234","Mien Nam")
# cur.execute(sql,values)
# myconn.commit()
# cur.execute("select * from Customers")
# for thing in cur.description:
#     print(thing)
# result=cur.fetchall()
# print(result)



# myconn.close()

class Customers(LabelFrame):
    def __init__(self,parent=None):
        LabelFrame.__init__(self,parent)
        
        self.parent = parent
        
        self.runUI()
    def runUI(self):
        self.parent.title("Customer")
        
        
        self.title_label=Label(self.parent,text="Codemy Customer Database",font=("Helvetica",16))
        self.title_label.grid(row=0,column=0,columnspan=2,pady="10")
        
        self.first_name=Label(self.parent,text="First Name")
        self.first_name.grid(row=1,column=0,sticky=W,padx="10")
        
        self.last_name=Label(self.parent,text="Last_Name")
        self.last_name.grid(row=2,column=0,sticky=W,padx="10")
        
        
        self.address2=Label(self.parent,text="Address 2")
        self.address2.grid(row=3,column=0,sticky=W,padx="10")
        
        
        self.address1=Label(self.parent,text="Address 1")
        self.address1.grid(row=4,column=0,sticky=W,padx="10")
        
        
        self.city=Label(self.parent,text="City")
        self.city.grid(row=5,column=0,sticky=W,padx="10")
        
        
        self.state=Label(self.parent,text="State")
        self.state.grid(row=6,column=0,sticky=W,padx="10")
        
        
        self.zipcode=Label(self.parent,text="Zipcode")
        self.zipcode.grid(row=7,column=0,sticky=W,padx="10")
        
        
        self.country=Label(self.parent,text="Country")
        self.country.grid(row=8,column=0,sticky=W,padx="10")
        
        
        self.phone=Label(self.parent,text="Phone")
        self.phone.grid(row=9,column=0,sticky=W,padx="10")
        
        
        self.email=Label(self.parent,text="Email")
        self.email.grid(row=10,column=0,sticky=W,padx="10")
        
        
        self.username=Label(self.parent,text="Username")
        self.username.grid(row=11,column=0,sticky=W,padx="10")
        
        self.payment_method=Label(self.parent,text="Payment Method")
        self.payment_method.grid(row=12,column=0,sticky=W,padx="10")
        
        self.discount_code=Label(self.parent,text="Discount Code")
        self.discount_code.grid(row=13,column=0,sticky=W,padx="10")
        
        self.price_paid=Label(self.parent,text="Price Paid")
        self.price_paid.grid(row=14,column=0,sticky=W,padx="10")
        
        self.first_name_box=Entry(self.parent)
        self.first_name_box.grid(row=1,column=1,pady=5)
        
        self.last_name_box=Entry(self.parent)
        self.last_name_box.grid(row=2,column=1,pady=5)
        
        self.address2_box=Entry(self.parent)
        self.address2_box.grid(row=3,column=1,pady=5)
        
        self.address1_box=Entry(self.parent)
        self.address1_box.grid(row=4,column=1,pady=5)
        
        self.city_box=Entry(self.parent)
        self.city_box.grid(row=5,column=1,pady=5)
        
        self.state_box=Entry(self.parent)
        self.state_box.grid(row=6,column=1,pady=5)
        
        self.zip_code_box=Entry(self.parent)
        self.zip_code_box.grid(row=7,column=1,pady=5)
        
        self.country_box=Entry(self.parent)
        self.country_box.grid(row=8,column=1,pady=5)
        
        self.email_box=Entry(self.parent)
        self.email_box.grid(row=9,column=1,pady=5)
        
        self.phone_box=Entry(self.parent)
        self.phone_box.grid(row=10,column=1,pady=5)
        
        self.user_name_box=Entry(self.parent)
        self.user_name_box.grid(row=11,column=1,pady=5)
        
        self.payment_method_box=Entry(self.parent)
        self.payment_method_box.grid(row=12,column=1,pady=5)
        
        self.discount_code_box=Entry(self.parent)
        self.discount_code_box.grid(row=13,column=1,pady=5)
        
        self.price_paid_box=Entry(self.parent)
        self.price_paid_box.grid(row=14,column=1,pady=5)
        
        self.add_customer_botton=Button(self.parent,text="Add Customers Database",command=self.add_customer)
        self.add_customer_botton.grid(row=15,column=0,padx=10,pady=10)
        
        self.clear_fields_botton=Button(self.parent,text="Clear Fields",command=self.clear_fields)
        self.clear_fields_botton.grid(row=15,column=1,padx=10,pady=10)
        
        self.list_customers_btn=Button(self.parent,text="List Customers",command=self.list_customers)
        self.list_customers_btn.grid(row=16,column=0,padx=10,pady=10,sticky=W)
        
        self.delete_row_btn=Button(self.parent,text="Delete Rows",command=self.delete_row)
        self.delete_row_btn.grid(row=16,column=1,padx=10,pady=10)
        
        self.search_customers_box=Button(self.parent,text="Search/Edit Customers",command=self.search_customers)
        self.search_customers_box.grid(row=17,column=0,padx=10,pady=10,sticky=W)
        
    def search_customers(self):
        root=Tk()
        root.title('List Search Customers')
        root.config(background="white")
        root.geometry("1200x800")
        def update_record():
            sql_command="""update Customers set first_name=%s,last_name=%s,zipcode=%s,price_paid=%s,user_id=%s,email=%s,address_1=%s,
            address_2=%s,city=%s,country=%s,phone=%s,payment_method=%s,discount_code=%s,state=%s where user_id=%s"""
            
            first_name=first_name_box.get()
            last_name=last_name_box.get()
            zipcode=zip_code_box.get()
            price_paid=price_paid_box.get()
            user_id=user_name_box.get()
            email=email_box.get()
            address_1=address1_box.get()
            address_2=address2_box.get()
            city=city_box.get()
            country=country_box.get()
            phone=phone_box.get()
            payment_method=payment_method_box.get()
            discount_code=discount_code_box.get()
            state=state_box.get()
            inputs=(first_name,last_name,zipcode,price_paid,user_id,email,address_1,address_2,city,country,phone,payment_method,discount_code,state,user_id)
            cur.execute(sql_command,inputs)
            myconn.commit()
            root.destroy()
            
        def edit_now(id,index):
            sql2="select*from Customers where user_id=%s"
            name2=(id,)
            result2=cur.execute(sql2,name2)
            result2=cur.fetchall()
            
            first_name=Label(root,text="First Name")
            first_name.grid(row=index+2,column=0,sticky=W,padx="10")
            
            
            last_name=Label(root,text="Last_Name")
            last_name.grid(row=index+3,column=0,sticky=W,padx="10")
            
            
            address2=Label(root,text="Address 2")
            address2.grid(row=index+4,column=0,sticky=W,padx="10")
            
            
            address1=Label(root,text="Address 1")
            address1.grid(row=index+5,column=0,sticky=W,padx="10")
            
            
            city=Label(root,text="City")
            city.grid(row=index+6,column=0,sticky=W,padx="10")
            
            
            state=Label(root,text="State")
            state.grid(row=index+7,column=0,sticky=W,padx="10")
            
            
            zipcode=Label(root,text="Zipcode")
            zipcode.grid(row=index+8,column=0,sticky=W,padx="10")
            
            
            country=Label(root,text="Country")
            country.grid(row=index +9,column=0,sticky=W,padx="10")
            
            
            phone=Label(root,text="Phone")
            phone.grid(row=index+10,column=0,sticky=W,padx="10")
            
            
            email=Label(root,text="Email")
            email.grid(row=index+11,column=0,sticky=W,padx="10")
            
            
            username=Label(root,text="Username")
            username.grid(row=index+12,column=0,sticky=W,padx="10")
            
            payment_method=Label(root,text="Payment Method")
            payment_method.grid(row=index+13,column=0,sticky=W,padx="10")
            
            discount_code=Label(root,text="Discount Code")
            discount_code.grid(row=index +14,column=0,sticky=W,padx="10")
            
            price_paid=Label(root,text="Price Paid")
            price_paid.grid(row=index+15,column=0,sticky=W,padx="10")
            
            global first_name_box
            first_name_box=Entry(root)
            first_name_box.grid(row=index+2,column=1,pady=5)
            first_name_box.insert(0,result2[0][0])
            
            global last_name_box
            last_name_box=Entry(root)
            last_name_box.grid(row=index+3,column=1,pady=5)
            last_name_box.insert(0,result2[0][1])
            
            global address2_box
            address2_box=Entry(root)
            address2_box.grid(row=index+4,column=1,pady=5)
            address2_box.insert(0,result2[0][6])
            
            global address1_box
            address1_box=Entry(root)
            address1_box.grid(row=index+5,column=1,pady=5)
            address1_box.insert(0,result2[0][7])
            
            global city_box
            city_box=Entry(root)
            city_box.grid(row=index+6,column=1,pady=5)
            city_box.insert(0,result2[0][8])
            
            global state_box
            state_box=Entry(root)
            state_box.grid(row=index+7,column=1,pady=5)
            state_box.insert(0,result2[0][13])
            
            global zip_code_box
            zip_code_box=Entry(root)
            zip_code_box.grid(row=index+8,column=1,pady=5)
            zip_code_box.insert(0,result2[0][2])
            
            global country_box
            country_box=Entry(root)
            country_box.grid(row=index+9,column=1,pady=5)
            country_box.insert(0,result2[0][9])
            
            global email_box
            email_box=Entry(root)
            email_box.grid(row=index +10,column=1,pady=5)
            email_box.insert(0,result2[0][10])
            
            global phone_box
            phone_box=Entry(root)
            phone_box.grid(row=index+11,column=1,pady=5)
            phone_box.insert(0,result2[0][5])
            global user_name_box
            user_name_box=Entry(root)
            user_name_box.grid(row=index+12,column=1,pady=5)
            user_name_box.insert(0,result2[0][4])
            
            global payment_method_box
            payment_method_box=Entry(root)
            payment_method_box.grid(row=index+13,column=1,pady=5)
            payment_method_box.insert(0,result2[0][11])
            
            global discount_code_box
            discount_code_box=Entry(root)
            discount_code_box.grid(row=index+14,column=1,pady=5)
            discount_code_box.insert(0,result2[0][12])
            
            global price_paid_box
            price_paid_box=Entry(root)
            price_paid_box.grid(row=index+15,column=1,pady=5)
            price_paid_box.insert(0,result2[0][3])
            
            
            save_record= Button(root,text="Update Record",command=update_record)
            save_record.grid(row=index+16,column=0,sticky=W,padx=10)
        
        def search_now():
            selected=drop.get()
            sql=""
            if selected=="Search by ...":
                test=Label(root,text="Hey! You forgot to pick a drop down colection")
                test.grid(row=3,column=0)
            if selected=="Last Name":
                
                sql="select* from Customers where last_name=%s"
            if selected=="Email Address":
                
                sql="select* from Customers where email=%s"
            if selected=="Customers ID":
                
                sql="select* from Customers where user_id=%s"
            searched=search_box.get()
            
            name=(searched,)
            result=cur.execute(sql,name)
            result=cur.fetchall()
            if not result:
                result="Record Not Found"
                search_label=Label(root,text=result,bg="white")
                search_label.grid(row=4,column=0,sticky=W)
            else:
                for index,x in enumerate(result):
                    num=0
                    index=+5
                    id_reference=str(x[4])
                    edit_button=Button(root,text="Edit",command=lambda: edit_now(id_reference,index))
                    edit_button.grid(row=index,column=num,sticky=W)
                    for y in x:
                        search_label=Label(root,text=y,bg="white")
                        search_label.grid(row=index,column=num+1,sticky=W)
                        num+=1
            csv_button= Button(root,text="Save To Excel",command=lambda:self.write_to_csv(result))
            csv_button.grid(row=index+1,column=0,sticky=W)
        
        search_box=Entry(root)
        search_box.grid(row=0,column=1,padx=10,pady=10)
        
        search_box_label=Label(root,text="Search")
        search_box_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        search_button=Button(root,text="Search Customers",command=search_now)
        search_button.grid(row=1,column=0,padx=10,sticky=W)

        drop=Combobox(root)
        drop["values"]=["Search by ...","Last Name","Email Address",'Customers ID']
        drop.current(0)
        drop.grid(row=0,column=2)
        
    
    def delete_row(self):
        
        cur.execute("delete from Customers where user_id = %s"%self.user_name_box.get())
        myconn.commit()
    def list_customers(self):
        self.root=Tk()
        self.root.title("Customers")
        labelfram_customers = LabelFrame(self.root,text="List Customers",bg="white")
        labelfram_customers.pack()
        cur.execute("select * from Customers")
        
        result=cur.fetchall()
        for index,x in enumerate(result):
            num=0
            for y in x:
                loookup_label=Label(labelfram_customers,text=y,bg="white")
                loookup_label.grid(row=index,column=num)
                num+=1
        csv_button= Button(labelfram_customers,text="Save To Excel",command=lambda:self.write_to_csv(result))
        csv_button.grid(row=index+1,column=0)
        

        self.root.geometry("800x600")
    
        
    def write_to_csv(self,result): 
        dlg = Directory(self)
        fl=dlg.show()
        global fpath
        fpath= os.path.join(fl,"customers.csv")
        with open(fpath,"w") as f:
            w=csv.writer(f,dialect="excel")
            for record in result:
                w.writerow(record)
        
        
    def add_customer(self):
        sql = ("insert into Customers(first_name,last_name,zipcode,price_paid,user_id,email,address_1,"
            "address_2,city,country,phone,payment_method,discount_code,state)" 
            "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        values=(self.first_name_box.get(),self.last_name_box.get(),self.zip_code_box.get(),self.price_paid_box.get(),self.user_name_box.get(),
                self.email_box.get(),self.address1_box.get(),self.address2_box.get(),self.city_box.get(),self.country_box.get(),
                self.phone_box.get(),self.payment_method_box.get(),self.discount_code_box.get(),self.state_box.get())
        print (values)
        print(sql)
        cur.execute(sql, values)


        myconn.commit()
        

    def clear_fields(self):
        self.first_name_box.delete(0,END)
        self.last_name_box.delete(0,END)
        self.address2_box.delete(0,END)
        self.address1_box.delete(0,END)
        self.city_box.delete(0,END)
        self.state_box.delete(0,END)
        self.zip_code_box.delete(0,END)
        self.country_box.delete(0,END)
        self.email_box.delete(0,END)
        self.phone_box.delete(0,END)
        self.user_name_box.delete(0,END)
        self.payment_method_box.delete(0,END)
        self.discount_code_box.delete(0,END)
        self.price_paid_box.delete(0,END)
        
root=Tk()
root.geometry("350x600")
app= Customers(root)
root.mainloop()