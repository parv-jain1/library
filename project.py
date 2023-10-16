def add():
    global b_id,top,b_name,b_author,b_no,b_cost
    top=Tk()
    top.geometry('1200x650')
    top.title('Add Books')
    top.configure(bg='yellow')
    Label(top,text='ADD BOOKS',font=("Helvetica", "32",'bold'),bg='blue',fg='yellow',relief='ridge',bd=20).pack(fill='x',side='top')
    l=Label(top,text='Book ID',font=('times','14','italic'),bg='yellow').place(relx=0.28,rely=0.3)
    b_id=Entry(top,width=50,bd=5)
    b_id.place(relx=0.45,rely=0.3)
    l=Label(top,text='Book Name',font=('times','14','italic'),bg='yellow').place(relx=0.28,rely=0.4)
    b_name=Entry(top,width=50,bd=5)
    b_name.place(relx=0.45,rely=0.4)
    l=Label(top,text=' Author Name',font=('times','14','italic'),bg='yellow')
    l.place(relx=0.28,rely=0.5)
    b_author=Entry(top,width=50,bd=5)
    b_author.place(relx=0.45,rely=0.5)
    l=Label(top,text='No of Copies',font=('times','14','italic'),bg='yellow')
    l.place(relx=0.28,rely=0.6)
    b_no=Entry(top,width=50,bd=5)
    b_no.place(relx=0.45,rely=0.6)
    l=Label(top,text='Cost of a Book',font=('times','14','italic'),bg='yellow')
    l.place(relx=0.28,rely=0.7)
    b_cost=Entry(top,width=50,bd=5)
    b_cost.place(relx=0.45,rely=0.7)
    Button(top,text='submit',bd=5,command=book,font=('33'),height=2,width=10).place(relx=0.35,rely=0.85)
    Button(top,text='back',bd=5,command=lambda:(top.destroy(),code()),font=('33'),height=2,width=10).place(relx=0.55,rely=0.85)
    top.mainloop()
    
def book():
    from tkinter import messagebox
    mys.execute('select book_id from books')
    b=mys.fetchall()
    bid=b_id.get()
    b_id.delete(0,END)
    title = (b_name.get()).title()
    b_name.delete(0,END)
    author = b_author.get()
    b_author.delete(0,END)
    no_of_copies = int(b_no.get())
    b_no.delete(0,END)
    cost = b_cost.get()
    b_cost.delete(0,END)
    issued=0
    sql = "INSERT INTO books (book_id,name, author,copies,cost,issued) VALUES (%s,%s,%s,%s,%s,%s)"
    try:
        b.index((bid,))
        mys.execute('update books set copies= copies+%s  where book_id="%s"'%(no_of_copies,bid))
        p.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        val = (bid,title, author,no_of_copies,cost,issued)
        mys.execute(sql,val)
        p.commit()
        messagebox.showinfo('Success',"Book added successfully")
        
def issue():
    global i,b_id,c_id,s_name,class_,date
    i=Tk()
    i.geometry('1200x650')
    i.title('Issue Books')
    i.configure(bg='yellow')
    Label(i,text='ISSUE BOOKS',font=("Helvetica", "32",'bold'),bg='blue',fg='yellow',relief='ridge',bd=20).pack(fill='x',side='top')
    Label(i,text='Book ID',font=('times','14','italic'),bg='yellow').place(relx=0.28,rely=0.3)
    b_id=Entry(i,width=50,bd=5)
    b_id.place(relx=0.45,rely=0.3)
    Label(i,text='student ID',font=('times','14','italic'),bg='yellow').place(relx=0.28,rely=0.4)
    c_id=Entry(i,width=50,bd=5)
    c_id.place(relx=0.45,rely=0.4)
    Label(i,text='Student Name',font=('times','14','italic'),bg='yellow').place(relx=0.28,rely=0.5)
    s_name=Entry(i,width=50,bd=5)
    s_name.place(relx=0.45,rely=0.5)
    Label(i,text='Student Class',font=('times','14','italic'),bg='yellow').place(relx=0.28,rely=0.6)
    class_=Entry(i,width=50,bd=5)
    class_.place(relx=0.45,rely=0.6)
    Button(i,text='submit',bd=5,command=book_issue,font=('33'),height=2,width=10).place(relx=0.35,rely=0.85)
    Button(i,text='back',bd=5,command=lambda:(i.destroy(),code()),font=('33'),height=2,width=10).place(relx=0.55,rely=0.85)    
    i.mainloop()
    
def book_issue():
    from tkinter import messagebox
    import datetime
    bid=b_id.get()
    mys.execute('select copies,issued from books WHERE book_id="%s"'%(bid))
    b=mys.fetchone()
    a=datetime.date.today()
    mys.execute('select book_id,student_id,return_status from issues where student_id="%s" and return_status="not returned"'%(bid,c_id.get()))
    c=mys.fetchall()
    if len(c):
        messagebox.showinfo('','book already issued to the customer')
    else:
        try:
            if b[1]<b[0]:
                mys.execute("UPDATE books SET issued = issued+%s WHERE book_id ='%s'"%(1,bid))
                p.commit()
                sql = "INSERT INTO issues(book_id ,student_id,student_name , Class ,Date,return_date,return_status) VALUES (%s,%s,%s,%s,%s,%s,%s) "
                val = (bid,int(c_id.get()),s_name.get(),class_.get(),a,'-','not returned')
                mys.execute(sql,val)
                p.commit()
                messagebox.showinfo('congrats','Book Issued')
            else:
                messagebox.showinfo('sorry!', 'all books issued')
        except:
            messagebox.showinfo('sorry!', 'Book doesnt Exist')
    b_id.delete(0,END)
    c_id.delete(0,END)
    s_name.delete(0,END)
    class_.delete(0,END)
    
def delete():
    global bid,b_id,t
    t=Tk()
    t.geometry('750x600')
    t.configure(bg='yellow')
    Label(t,text='Delete Books',font=("Helvetica", "32",'bold'),bg='#42E0D1',fg='yellow',relief='ridge',bd=20).pack(fill='x',side='top')
    Label(t,text='Book Id',font=('times','14','italic'),bg='yellow').place(relx=0.25,rely=0.35)
    b_id=Entry(t,width=50,bd=5)
    b_id.place(relx=0.38,rely=0.35)
    Button(t,text='submit',bd=5,command=booksdel,font=('33'),height=2,width=10).place(relx=0.35,rely=0.85)
    Button(t,text='back',bd=5,command=lambda:(t.destroy(),code()),font=('33'),height=2,width=10).place(relx=0.55,rely=0.85)
    t.mainloop()

def booksdel():
    from tkinter import messagebox
    mys.execute('select book_id from books')
    b=mys.fetchall()
    if (b_id.get(),) in b :
        mys.execute('delete from books WHERE book_id="%s"'%(b_id.get(),))
        p.commit()
        mys.execute('delete from issues WHERE book_id="%s"'%(b_id.get(),))
        p.commit()
        messagebox.showinfo('done','book deleted')
    else:
        messagebox.showinfo('check again','book doesnt exist')
    b_id.delete(0,END)

def Return():
    global b_id,c_id,r_date
    r=Tk()
    r.geometry('1200x650')
    r.configure(bg='yellow')
    Label(r,text='Return books',font=("Helvetica", "32",'bold'),bg='#42E0D1',fg='yellow',relief='ridge',bd=20).pack(fill='x',side='top')
    Label(r,text='Book Id',font=('times','14','italic'),bg='yellow').place(relx=0.20,rely=0.35)
    b_id=Entry(r,width=50,bd=5)
    b_id.place(relx=0.38,rely=0.35)
    Label(r,text='student Id',font=('times','14','italic'),bg='yellow').place(relx=0.20,rely=0.45)
    c_id=Entry(r,width=50,bd=5)
    c_id.place(relx=0.38,rely=0.45)
    Label(r,text='Return Date(yyyy-mm-dd)',font=('times','14','italic'),bg='yellow').place(relx=0.20,rely=0.55)
    r_date=Entry(r,width=50,bd=5)
    r_date.place(relx=0.38,rely=0.55)
    Button(r,text='submit',bd=5,command=returnbooks,font=('33'),height=2,width=10).place(relx=0.35,rely=0.85)
    Button(r,text='Back',bd=5,command=lambda:(r.destroy(),code()),font=('33'),height=2,width=10).place(relx=0.55,rely=0.85)
    r.mainloop()
    
def returnbooks():
    from tkinter import messagebox
    from datetime import datetime
    mys.execute('select book_id,student_id,return_status from issues')
    q=mys.fetchall()
    if (b_id.get() ,int(c_id.get()),'not returned') in q :
        mys.execute('update issues set return_date="%s" where book_id="%s" and student_id="%s" and return_status="not returned"'%(r_date.get(),b_id.get(),c_id.get()))
        p.commit()
        mys.execute('update issues set return_status="returned" where book_id="%s" and student_id="%s"'%(b_id.get(),c_id.get()))
        p.commit()
        mys.execute('update books set issued=issued-%s where book_id="%s"'%(1,b_id.get()))
        p.commit()
        mys.execute('select Date from issues where book_id="%s" and student_id="%s" and return_date="%s"'%(b_id.get(),c_id.get(),r_date.get()))
        sd=mys.fetchall()
        sd=sd[0][0]
        df=datetime.strptime(r_date.get(),"%Y-%m-%d")
        df=datetime.date(df)
        de=(df-sd).days
        if int(de)>7:
            c=(de-7)*50
            mys.execute('update issues set fine=%s where book_id="%s" and student_id="%s" and return_date="%s"'%(c,b_id.get(),c_id.get(),r_date.get()))
            p.commit()
            messagebox.showinfo('',f'book returned please pay {c} as fine')
        else:
            messagebox.showinfo('','book returned')
    else:
        messagebox.showinfo('check again','book not issued')
    b_id.delete(0,END)
    c_id.delete(0,END)
    r_date.delete(0,END)
        
def details():
    d=Tk()
    d.geometry('600x600')
    d.configure(bg='yellow')
    Label(d,text='Details',font=("Helvetica", "32",'bold'),bg='#42E0D1',fg='yellow',relief='ridge',bd=20).pack(fill='x',side='top')
    Button(d,text='Book Details',width=20,height=2,command=detailsbooks,bg='blue',fg='white',font='10',bd=5).pack(pady=20)
    Button(d,text='Issue Details',width=20,height=2,command=detailsissues,bg='blue',fg='white',font='10',bd=5).pack(pady=20)
    Button(d,text='back',width=20,height=1,command=lambda:(d.destroy(),code()),bg='blue',fg='white',font='10',bd=5).pack(pady=20)
    d.mainloop()
    
def detailsbooks():
    from tkinter import messagebox
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate
    from reportlab.platypus.tables import Table,TableStyle,colors
    mys.execute('select * from books')
    a=[('book id','name','author','copies','cost','issues')]+mys.fetchall()
    my_path='books.pdf'
    my_doc=SimpleDocTemplate(my_path,pagesize=A4,title='Books')
    c_width=[1*inch,1.5*inch,1*inch,1*inch,1*inch]
    t=Table(a,rowHeights=20,repeatRows=1,colWidths=c_width)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightgreen),('FONTSIZE',(0,0),(-1,-1),10)]))
    elements=[]
    elements.append(t)
    my_doc.build(elements)
    messagebox.showinfo('','data saved in storage')

def detailsissues():
    from tkinter import messagebox
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate
    from reportlab.platypus.tables import Table,TableStyle,colors
    mys.execute('select * from issues')
    a=[('book id' ,'student id','student name' , 'Class' ,'Date','return date','return status')]+mys.fetchall()
    my_path='issues.pdf'
    my_doc=SimpleDocTemplate(my_path,pagesize=A4,title='Issues')
    c_width=[1*inch,1.5*inch,1*inch,1*inch,1*inch,1*inch,1*inch]
    t=Table(a,rowHeights=20,repeatRows=1,colWidths=c_width)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightgreen),('FONTSIZE',(0,0),(-1,-1),10)]))
    elements=[]
    elements.append(t)
    my_doc.build(elements)
    messagebox.showinfo('','data saved in storage')

def view():
    n=Tk()
    n.geometry('1200x650')
    n.configure(bg='red')
    Label(n, text="%-30s%-50s%-40s%-30s%-40s%-40s"%('BID','Title','Author','copies','cost','issued'),bg='yellow',font=('times','12','italic')).place(relx=0.01,rely=0.05)
    mys.execute('select * from books')
    q=mys.fetchall()
    y=0.1
    for i in q:
            Label(n,text="%-30s%-50s%-40s%-30s%-40s%-40s"%(i[0],i[1],i[2],i[3],i[4],i[5]) ,bg='black', fg='white',font=('times','12','italic')).place(relx=0.01,rely=y)
            y += 0.05
    Button(n,text='back',width=20,height=1,command=lambda:(n.destroy(),code()),bg='blue',fg='white',font='10',bd=5).place(relx=0.9,rely=0.9)
    n.mainloop()
    
def code():
    global r
    r=Tk()
    r.geometry('1200x650')
    r.configure(bg='#42E0D1')
    r.title('library management system')
    Label(r,text='Library Management System',font=("Helvetica", "34",'bold'),bg='#42E0D1',fg='yellow',relief='ridge',bd=20).pack(fill='x',side='top')
    Button(r,text='Add Books',width=20,height=1,command=lambda:(r.destroy(),add()),bg='blue',fg='white',font='10',bd=5).pack(pady=15)
    Button(r,text='Delete Books',width=20,height=1,command=lambda:(r.destroy(),delete()),bg='blue',fg='white',font='10',bd=5).pack(pady=15)
    Button(r,text='View Books',width=20,height=1,command=lambda:(r.destroy(),view()),bg='blue',fg='white',font='10',bd=5).pack(pady=15)
    Button(r,text='Return Books',width=20,height=1,command=lambda:(r.destroy(),Return()),bg='blue',fg='white',font='10',bd=5).pack(pady=15)
    Button(r,text='Details',width=20,height=1,command=lambda:(r.destroy(),details()),bg='blue',fg='white',font='10',bd=5).pack(pady=15)
    Button(r,text='Lend Books',width=20,height=1,command=lambda:(r.destroy(),issue()),bg='blue',fg='white',font='10',bd=5).pack(pady=15)
    Button(r,text='Quit',width=20,height=1,command=r.destroy,bg='blue',fg='white',font='10',bd=5).pack(pady=15)
    r.mainloop()
    
if __name__=='__main__' :
    from tkinter import *
    import mysql
    from mysql import connector
    import csv
    p=mysql.connector.connect(host='localhost',user='root',password='parvjain@1234')
    mys=p.cursor()
    try:
        mys.execute('create database library')
    except:
        pass
    p.database='library'
    try:
        mys.execute('create table books (book_id VARCHAR(8), name VARCHAR(255), author VARCHAR(255),copies int,cost int,issued int)')
    except:
        pass
    try:
        mys.execute('create table issues (book_id VARCHAR(8),student_id int,student_name VARCHAR(255), Class VARCHAR(10),Date DATE,return_date varchar(255) ,return_status VARCHAR (255))') 
    except:
        pass
    code()
    p.close()
