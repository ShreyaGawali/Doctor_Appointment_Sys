from tkinter import *
from tkinter import messagebox
import cx_Oracle
cx_Oracle.init_oracle_client()
con=cx_Oracle.connect("dsoft/abcd@localhost/XE")
print("connected successfully")
cur=con.cursor()

ids = []

class Application:
    def __init__(self, master):
        self.master = master
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text="KEM Hospital Appointments", font=('arial 40 bold'), fg='black', bg='pink')
        self.heading.place(x=0, y=0)
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=100)
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.age.place(x=0, y=140)
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.gender.place(x=0, y=180)
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.location.place(x=0, y=220)
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.time.place(x=0, y=260)
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.phone.place(x=0, y=300)

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)
        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)
        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)
        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)
        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)
        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=340)

        sql2 = "SELECT ID FROM appointments "
        self.result = cur.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            if self.id is not None:
                ids.append(self.id)

        if ids:  # Check if the ids list is not empty
            self.new = sorted(ids)
            self.final_id = self.new[len(ids) - 1]

        #self.new = sorted(ids)
        #self.final_id = self.new[len(ids)-1]
            self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
            self.logs.place(x=0, y=0)
            self.box = Text(self.right, width=50, height=40)
            self.box.place(x=20, y=60)
            self.box.insert(END, "Total Appointments till now :  " + str(self.final_id))

    def add_appointment(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            sql = "INSERT INTO appointments (name, age, gender, location, scheduled_time, phone) VALUES (:1, :2, :3, :4, :5, :6)"
            cur.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            con.commit()
            messagebox.showinfo("Success", "Appointment for " + str(self.val1) + " has been created")
            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))


root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()
