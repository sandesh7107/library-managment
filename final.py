from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connection import *


class Gui:
    def __init__(self):
        self.stu = Student()

        self.db = sandesh()
        self.update_index = ''
        self.update1_index = ''

    def aa(self):
        try:
            self.wn = Tk()
            self.wn.geometry('500x500')
            self.wn.title('library management system')
            self.wn.configure(bg='green')
            self.main = Label(self.wn, text="Dashboard ", bg='yellow', fg='green', font=('Ariel', 16, 'italic'))
            self.main.place(x=180, y=20)

            self.san = Button(self.wn, text='register', font=('Ariel', 20, 'italic'), bg='pink', command=self.register)
            self.san.place(x=180, y=150)
            self.san1 = Button(self.wn, text='login', font=('Ariel', 20, 'italic'), bg='pink', command=self.login)
            self.san1.place(x=180, y=220)
            self.wn.mainloop()
        except Exception as e:
            print(e)

    def register(self):
        try:
            self.wn1 = Tk()
            self.wn1.geometry('700x700')
            self.wn1.title('library management system')
            self.wn1.configure(bg='pink')
            self.name = Label(self.wn1, text="Details ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.name.place(x=200, y=5)
            self.name = Label(self.wn1, text="Name", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.name.place(x=100, y=40)

            self.name_ent = Entry(self.wn1, font=('Ariel', 14, 'italic'))
            self.name_ent.place(x=200, y=40)
            self.address = Label(self.wn1, text="Address", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.address.place(x=100, y=100)
            self.address_ent = Entry(self.wn1, font=('Ariel', 14, 'italic'))
            self.address_ent.place(x=200, y=100)
            self.contact = Label(self.wn1, text="Contact", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.contact.place(x=100, y=150)
            self.contact_ent = Entry(self.wn1, font=('Ariel', 14, 'italic'))
            self.contact_ent.place(x=200, y=150)
            self.email = Label(self.wn1, text="Email", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.email.place(x=100, y=200)
            self.email_ent = Entry(self.wn1, font=('Ariel', 14, 'italic'))
            self.email_ent.place(x=200, y=200)
            self.user_name = Label(self.wn1, text="User Name", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.user_name.place(x=100, y=250)
            self.user_name_ent = Entry(self.wn1, font=('Ariel', 14, 'italic'))
            self.user_name_ent.place(x=225, y=250)
            self.password = Label(self.wn1, text="Password", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.password.place(x=100, y=300)
            self.password_ent = Entry(self.wn1, font=('Ariel', 14, 'italic'))
            self.password_ent.place(x=220, y=300)
            self.samir = Button(self.wn1, text='Save', font=('Ariel', 14, 'italic'), command=self.register_user)

            self.samir.place(x=250, y=350)

            self.samir1 = Button(self.wn1, text='Back', font=('Ariel', 14, 'italic'), command=self.undo)

            self.samir1.place(x=350, y=350)
            self.wn.destroy()
            self.wn1.mainloop()
        except Exception as e:
            print(e)

    def undo(self):
        self.wn1.destroy()
        self.aa()

    def register_user(self):
        try:
            self.db = sandesh()
            name = self.name_ent.get()
            email = self.email_ent.get()
            address = self.address_ent.get()
            contact = self.contact_ent.get()

            un = self.user_name_ent.get()
            pw = self.password_ent.get()
            if name == '' or email == '' or contact == '' or un == '' or pw == '' or address == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''insert into admin_reg (name, email, contact, username, password,address) values(%s,%s,%s,%s,%s,%s)'''
                vals = (name, email, contact, un, pw, address)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Register Successful!')
        except Exception as e:
            print(e)

    def login(self):
        try:
            self.wn2 = Tk()
            self.wn2.geometry('700x700')
            self.wn2.title('library management system')
            self.wn2.configure(bg='red')

            self.name = Label(self.wn2, text="Fill the requirements  ", bg='yellow', fg='blue',
                              font=('Ariel', 14, 'italic'))
            self.name.place(x=200, y=150)
            self.user_name = Label(self.wn2, text="User Name", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.user_name.place(x=100, y=250)
            self.user_name_ent = Entry(self.wn2, font=('Ariel', 14, 'italic'))
            self.user_name_ent.place(x=225, y=250)
            self.password = Label(self.wn2, text="Password", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.password.place(x=100, y=300)
            self.password_ent = Entry(self.wn2, show='*', font=('Ariel', 14, 'italic'))
            self.password_ent.place(x=220, y=300)
            self.submit = Button(self.wn2, text='Login', font=('Ariel', 14, 'italic'), command=self.login_user)
            self.submit.place(x=100, y=350)
            self.wn.destroy()
            self.wn2.mainllop()
        except Exception as e:
            print(e)

    def login_user(self):
        try:
            self.db = sandesh()

            username1 = self.user_name_ent.get()
            password1 = self.password_ent.get()
            if username1 == '' or password1 == '':
                messagebox.showerror('Error', 'Enter username or password')
            else:
                qry = '''select * from admin_reg where username=%s and password=%s'''
                vals = (username1, password1)
                data_return = self.db.get_data_p(qry, vals)
                print(len(data_return))
                print(data_return)

                if len(data_return) == 0:
                    messagebox.showerror('Error', 'Wrong username or password')
                else:
                    messagebox.showinfo('Done', 'Login Successful')
                    self.dashboard()
        except Exception as e:
            print(e)








    def dashboard(self):
        try:
            self.stu = Student()
            self.bok = Book()

            self.wn3 = Tk()
            self.wn3.geometry('400x400')

            self.wn3.title('Library management system')
            self.wn3.configure(bg='red')
            self.Dashboard = Label(self.wn3, text="Dashboard", font=('Ariel', 14, 'italic'))
            self.Dashboard.pack(padx=10, pady=30)
            self.student_name = Button(self.wn3, text="Student Name", bg='yellow', fg='blue', font=('Ariel', 14),
                                       command=self.stu.student_name1)
            self.student_name.pack(padx=10, pady=10)
            self.book_name = Button(self.wn3, text="Book Name", bg='yellow', fg='blue', font=('Ariel', 14),
                                    command=self.bok.book_name1)
            self.book_name.pack(padx=10, pady=10)
            self.wn2.destroy()
            self.wn3.mainloop()
        except Exception as e:
            print(e)


class Student:
    def __init__(self):
        pass

    def student_name1(self):
        try:
            self.wn4 = Tk()
            self.wn4.geometry('1900x800')
            self.wn4.title('Library management system')
            self.wn4.configure(bg='red')

            self.name = Label(self.wn4, text="Student Details ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.name.place(x=200, y=5)
            self.stu_name = Label(self.wn4, text="Student Name", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.stu_name.place(x=100, y=50)
            self.stu_name_ent = Entry(self.wn4, font=('Ariel', 14, 'italic'))
            self.stu_name_ent.place(x=250, y=50)
            self.stu_id = Label(self.wn4, text="Student ID", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.stu_id.place(x=100, y=100)
            self.stu_id_ent = Entry(self.wn4, font=('Ariel', 14, 'italic'))
            self.stu_id_ent.place(x=250, y=100)
            self.address = Label(self.wn4, text="Address", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.address.place(x=100, y=150)
            self.address_ent = Entry(self.wn4, font=('Ariel', 14, 'italic'))
            self.address_ent.place(x=250, y=150)
            self.phone = Label(self.wn4, text="Contact Number", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.phone.place(x=100, y=200)
            self.phone_ent = Entry(self.wn4, font=('Ariel', 14, 'italic'))
            self.phone_ent.place(x=250, y=200)
            self.department = Label(self.wn4, text="Department", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.department.place(x=100, y=250)
            self.label = Label(self.wn4, text='Search', font=('Ariel', 14, 'italic'))
            self.label.place(x=500, y=500)
            a = ['Student Name', 'Student Id', 'Department']
            self.akash12 = ttk.Combobox(self.wn4, font=('Ariel', 14, 'italic'), values=a)
            self.akash12.place(x=600, y=450)

            ss = ['Physics', 'Chemistry', 'Biology', 'Maths', 'Computer science']
            self.department_ent = ttk.Combobox(self.wn4, font=('Ariel', 14, 'italic'), values=ss)
            self.department_ent.place(x=250, y=250)
            self.akash = Button(self.wn4, text='Select', font=('Ariel', 12, 'italic'), bg='yellow', command=self.search)
            self.akash.place(x=850, y=450)
            self.submit = Button(self.wn4, text="Save ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'),
                                 command=self.student_user)
            self.submit.place(x=20, y=300)
            self.submit = Button(self.wn4, text="Update ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'),
                                 command=self.student_update)
            self.submit.place(x=100, y=300)
            self.submit = Button(self.wn4, text="Delete ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'),
                                 command=self.student_delete)
            self.submit.place(x=200, y=300)
            self.submit = Button(self.wn4, text="Back", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'),
                                 command=self.undo)
            self.submit.place(x=300, y=300)
            self.aaa_tree = ttk.Treeview(self.wn4, column=('a', 'b', 'c', 'd', 'e'), height=17)
            self.aaa_tree.place(x=500, y=50)
            self.aaa_tree['show'] = 'headings'
            self.aaa_tree.column('a', width=200)
            self.aaa_tree.column('b', width=200)
            self.aaa_tree.column('c', width=200)
            self.aaa_tree.column('d', width=200)
            self.aaa_tree.column('e', width=200)

            self.aaa_tree.heading('a', text='Student Name')
            self.aaa_tree.heading('b', text='Student ID')
            self.aaa_tree.heading('c', text='Address')
            self.aaa_tree.heading('d', text='Contact Number')
            self.aaa_tree.heading('e', text='Department')
            self.showdata()

            self.wn4.mainloop()
        except Exception as e:
            print(e)

    def undo(self):
        self.wn4.destroy()

    def search(self):
        try:
            data = self.akash12.get()

            if data == '':
                messagebox.showerror('error', 'Select first!')
            elif data == 'Student Name':

                self.ent1 = Entry(self.wn4, font=('Ariel', 14, 'italic'))
                self.ent1.place(x=600, y=500)
                self.ent2 = Button(self.wn4, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_student_name)
                self.ent2.place(x=850, y=500)

            elif data == 'Student Id':

                self.ent1 = Entry(self.wn4, font=('Ariel', 14, 'italic'))
                self.ent1.place(x=600, y=500)
                self.ent2 = Button(self.wn4, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_student_id)
                self.ent2.place(x=850, y=500)

            elif data == 'Department':

                self.ent1 = Entry(self.wn4, font=('Ariel', 14, 'italic'))
                self.ent1.place(x=600, y=500)
                self.ent2 = Button(self.wn4, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_department)
                self.ent2.place(x=850, y=500)
        except Exception as e:
            print(e)

    def searchby_student_name(self):
        try:
            self.db = sandesh()

            keyword = self.ent1.get()
            qry = "SELECT * FROM student WHERE student_name LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.aaa_tree.delete(*self.aaa_tree.get_children())
            for i in data:
                self.aaa_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.aaa_tree.bind('<Double-1>', self.select_student)
        except Exception as e:
            print(e)

    def searchby_student_id(self):
        try:
            self.db = sandesh()

            keyword = self.ent1.get()
            qry = "SELECT * FROM student WHERE student_id LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.aaa_tree.delete(*self.aaa_tree.get_children())
            for i in data:
                self.aaa_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.aaa_tree.bind('<Double-1>', self.select_student)
        except Exception as e:
            print(e)

    def searchby_department(self):
        try:
            self.db = sandesh()

            keyword = self.ent1.get()
            qry = "SELECT * FROM student WHERE department LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.aaa_tree.delete(*self.aaa_tree.get_children())
            for i in data:
                self.aaa_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.aaa_tree.bind('<Double-1>', self.select_student)
        except Exception as e:
            print(e)

    def student_user(self):
        try:
            stu_name = self.stu_name_ent.get()
            stu_id = self.stu_id_ent.get()
            address = self.address_ent.get()

            department = self.department_ent.get()
            phone = self.phone_ent.get()

            if stu_name == '' or address == '' or department == '' or phone == '' or stu_id == '':
                messagebox.showerror('Error', 'Fill up all entries!')

            else:
                qry = '''insert into student (student_name, student_id, address, contact, department) values(%s,%s,%s,%s,%s)'''
                vals = (stu_name, stu_id, address, phone, department)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'student details saved')
                self.showdata()

        except Exception as e:
            print(e)


    def button(self):
        try:
            ab = self.stu_name_ent.get()

            self.bipin = Label(self.wn4, text=ab, bg='yellow', fg='blue', font=('Ariel', 14, 'bold'))
            self.bipin.place(x=30, y=100)
            self.wn4.mainloop()
        except Exception as e:
            print(e)

    def student_update(self):
        try:
            stu_name = self.stu_name_ent.get()

            stu_id = self.stu_id_ent.get()
            address = self.address_ent.get()

            phone = self.phone_ent.get()
            department = self.department_ent.get()

            id = (self.update1_index)
            print(type(id))
            if stu_name == '' or address == '' or department == '' or phone == '' or stu_id == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''update student SET student_name=%s, student_id=%s, address=%s, contact=%s, department=%s
                         WHERE id=%s'''
                vals = (stu_name, stu_id, address, phone, department, id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Update Successful!')
                self.showdata()
        except Exception as e:
            print(e)

    def student_delete(self):
        try:
            self.db = sandesh()

            id = [(self.update1_index)]
            print(type(id))
            if id == '':
                messagebox.showerror('Error', 'select item first')
            else:
                qry = '''delete from student where id=%s'''
                vals = (id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Delete Successful!')
                self.showdata()
        except Exception as e:
            print(e)

    def showdata(self):
        try:
            self.db = sandesh()
            qry = '''select * from student'''

            getresult = self.db.get_data(qry)
            print(getresult)
            self.aaa_tree.delete(*self.aaa_tree.get_children())
            for i in getresult:
                self.aaa_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.aaa_tree.bind('<Double-1>', self.select_student)
        except Exception as e:
            print(e)

    def select_student(self, event):
        try:
            row_selected = self.aaa_tree.selection()[0]
            select_p = self.aaa_tree.item(row_selected)
            self.update1_index = self.aaa_tree.item(row_selected, 'text')
            selected_data = self.aaa_tree.item(row_selected, 'values')
            self.stu_name_ent.delete(0, 'end')
            self.stu_name_ent.insert(0, selected_data[0])
            self.address_ent.delete(0, 'end')
            self.address_ent.insert(0, selected_data[2])

            self.stu_id_ent.delete(0, 'end')
            self.stu_id_ent.insert(0, selected_data[1])
            self.phone_ent.delete(0, 'end')
            self.phone_ent.insert(0, selected_data[3])

            self.department_ent.delete(0, 'end')
            self.department_ent.insert(0, selected_data[4])
        except Exception as e:
            print(e)


class Book:
    def __init__(self):
        pass

    def book_name1(self):
        try:
            self.wn5 = Tk()
            self.wn5.geometry('1900x900')
            self.wn5.title('Library management system')
            self.wn5.configure(bg='red')
            self.wn5.configure(bg='red')

            self.name = Label(self.wn5, text="Book Details ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.name.place(x=200, y=5)
            self.book_name = Label(self.wn5, text="Book Name", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.book_name.place(x=100, y=50)
            self.book_name_ent = Entry(self.wn5, font=('Ariel', 14, 'italic'))
            self.book_name_ent.place(x=250, y=50)
            self.borrow = Label(self.wn5, text="Borrow Date", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.borrow.place(x=100, y=100)
            self.borrow_ent = Entry(self.wn5, font=('Ariel', 14, 'italic'))
            self.borrow_ent.place(x=250, y=100)
            self.due = Label(self.wn5, text="Due Date", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.due.place(x=100, y=150)
            self.due_ent = Entry(self.wn5, font=('Ariel', 14, 'italic'))
            self.due_ent.place(x=250, y=150)
            self.loan = Label(self.wn5, text="Days on Loan", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.loan.place(x=100, y=200)
            self.loan_ent = Entry(self.wn5, font=('Ariel', 14, 'italic'))
            self.loan_ent.place(x=250, y=200)
            self.fine = Label(self.wn5, text="Late Return Fine", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.fine.place(x=100, y=250)
            self.fine_ent = Entry(self.wn5, font=('Ariel', 14, 'italic'))
            self.fine_ent.place(x=260, y=250)
            self.author = Label(self.wn5, text="Author", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'))
            self.author.place(x=100, y=300)
            self.author_ent = Entry(self.wn5, font=('Ariel', 14, 'italic'))
            self.author_ent.place(x=260, y=300)
            self.label = Label(self.wn5, text='Search', font=('Ariel', 14, 'italic'))
            self.label.place(x=500, y=500)
            b = ['Book Name', 'Due Date']
            self.akash34 = ttk.Combobox(self.wn5, font=('Ariel', 14, 'italic'), values=b)
            self.akash34.place(x=600, y=450)
            self.akash1 = Button(self.wn5, text='Select', font=('Ariel', 12, 'italic'), bg='yellow',
                                 command=self.search1)
            self.akash1.place(x=850, y=450)

            self.submit = Button(self.wn5, text="Save ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'),
                                 command=self.book_user)
            self.submit.place(x=20, y=350)
            self.submit1 = Button(self.wn5, text="update ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'),
                                  command=self.book_update)
            self.submit1.place(x=100, y=350)
            self.submit2 = Button(self.wn5, text="Delete ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'),
                                  command=self.book_delete)
            self.submit2.place(x=200, y=350)
            self.submit3 = Button(self.wn5, text="Back ", bg='yellow', fg='blue', font=('Ariel', 14, 'italic'),
                                  command=self.undo)
            self.submit3.place(x=300, y=350)
            self.bbb_tree = ttk.Treeview(self.wn5, column=('a', 'b', 'c', 'd', 'e', 'f'), height=17)
            self.bbb_tree.place(x=500, y=50)
            self.bbb_tree['show'] = 'headings'
            self.bbb_tree.column('a', width=150)
            self.bbb_tree.column('b', width=150)
            self.bbb_tree.column('c', width=150)
            self.bbb_tree.column('d', width=150)
            self.bbb_tree.column('e', width=150)
            self.bbb_tree.column('f', width=150)

            self.bbb_tree.heading('a', text='Book Name')
            self.bbb_tree.heading('b', text='Borrow Book')
            self.bbb_tree.heading('c', text='Due Date')
            self.bbb_tree.heading('d', text='Days On Loan')
            self.bbb_tree.heading('e', text='Late Return Fine')
            self.bbb_tree.heading('f', text='Author')
            self.showdata1()

            self.wn5.mainloop()
        except Exception as e:
            print(e)
    def undo(self):
        self.wn5.destroy()

    def search1(self):
        try:

            data = self.akash34.get()

            if data == '':
                messagebox.showerror('error', 'Select first!')
            elif data == 'Book Name':

                self.ent3 = Entry(self.wn5, font=('Ariel', 14, 'italic'))
                self.ent3.place(x=600, y=500)
                self.ent4 = Button(self.wn5, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_book_name)
                self.ent4.place(x=850, y=500)
            elif data == 'Due Date':

                self.ent3 = Entry(self.wn5, font=('Ariel', 14, 'italic'))
                self.ent3.place(x=600, y=500)
                self.ent4 = Button(self.wn5, text='Search', font=('Ariel', 14, 'italic'),
                                   command=self.searchby_due_date)
                self.ent4.place(x=850, y=500)
        except Exception as e:
            print(e)

    def searchby_book_name(self):
        try:
            self.db = sandesh()

            keyword = self.ent3.get()
            qry = "SELECT * FROM book WHERE book_name LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.bbb_tree.delete(*self.bbb_tree.get_children())
            for i in data:
                self.bbb_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
                self.bbb_tree.bind('<Double-1>', self.select_book)
        except Exception as e:
            print(e)

    def searchby_due_date(self):
        try:
            self.db = sandesh()

            keyword = self.ent3.get()
            qry = "SELECT * FROM book WHERE due_date LIKE '" + keyword + "%'"
            values = (keyword)
            data = self.db.get_data_p(qry, values)
            self.bbb_tree.delete(*self.bbb_tree.get_children())
            for i in data:
                self.bbb_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
                self.bbb_tree.bind('<Double-1>', self.select_book)
        except Exception as e:
            print(e)

    def book_user(self):
        try:
            self.db = sandesh()
            book_name = self.book_name_ent.get()
            bb = self.borrow_ent.get()

            due_date = self.due_ent.get()
            days_loan = self.loan_ent.get()
            fine = self.fine_ent.get()
            author = self.author_ent.get()

            if book_name == '' or bb == '' or due_date == '' or days_loan == '' or fine == '' or author == '':
                messagebox.showerror('Error', 'Fill up all entries!')
            else:
                qry = '''insert into book (book_name, borrow_date,due_date,loan_day,fine,author) values(%s,%s,%s,%s,%s,%s)'''
                vals = (book_name, bb, due_date, days_loan, fine, author)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'book details saved!')
                self.showdata1()
        except Exception as e:
            print(e)

    def button1(self):
        try:
            ac = self.book_name_ent.get()

            self.bipin2 = Label(self.wn5, text=ac, bg='yellow', fg='blue', font=('Ariel', 14, 'bold'))
            self.bipin2.place(x=30, y=100)
            self.wn5.mainloop()
        except Exception as e:
            print(e)

    def book_update(self):
        try:
            self.db = sandesh()
            book_name = self.book_name_ent.get()
            bb = self.borrow_ent.get()

            due_date = self.due_ent.get()
            days_loan = self.loan_ent.get()
            fine = self.fine_ent.get()
            author = self.author_ent.get()
            id = (self.update1_index)
            print(type(id))

            if book_name == '' or bb == '' or due_date == '' or days_loan == '' or fine == '' or author == '':
                messagebox.showerror('Error', 'Fill up all entries!')

            else:
                qry = '''update book SET book_name=%s, borrow_date=%s,  due_date=%s,  loan_day=%s,fine=%s,author=%s
                        WHERE id=%s'''
                vals = (book_name, bb, due_date, days_loan, fine, author, id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Update Successful!')
                self.showdata1()
        except Exception as e:
            print(e)

    def book_delete(self):
        try:

            self.db = sandesh()

            id = [(self.update1_index)]
            print(type(id))
            if id == '':
                messagebox.showerror('Error', 'select item first')
            else:
                qry = '''delete from book where id=%s'''
                vals = (id)
                self.db.iud(qry, vals)
                messagebox.showinfo('Done', 'Delete Successful!')
                self.showdata1()
        except Exception as e:
            print(e)

    def showdata1(self):
        try:
            self.db = sandesh()

            qry = '''select * from book'''
            getresult1 = self.db.get_data(qry)
            print(getresult1)
            self.bbb_tree.delete(*self.bbb_tree.get_children())
            for i in getresult1:
                self.bbb_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
                self.bbb_tree.bind('<Double-1>', self.select_book)
        except Exception as e:
            print(e)

    def select_book(self, event):
        try:
            row_selected = self.bbb_tree.selection()[0]
            select_p = self.bbb_tree.item(row_selected)
            self.update1_index = self.bbb_tree.item(row_selected, 'text')
            selected_data = self.bbb_tree.item(row_selected, 'values')
            self.book_name_ent.delete(0, 'end')
            self.book_name_ent.insert(0, selected_data[0])
            self.borrow_ent.delete(0, 'end')
            self.borrow_ent.insert(0, selected_data[1])

            self.due_ent.delete(0, 'end')
            self.due_ent.insert(0, selected_data[2])
            self.loan_ent.delete(0, 'end')
            self.loan_ent.insert(0, selected_data[3])

            self.fine_ent.delete(0, 'end')
            self.fine_ent.insert(0, selected_data[4])
            self.author_ent.delete(0, 'end')
            self.author_ent.insert(0, selected_data[5])
        except Exception as e:
            print(e)


cc=Gui()
cc.aa()