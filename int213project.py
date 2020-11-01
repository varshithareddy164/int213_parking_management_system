from tkinter import* 
screen=Tk()
screen.title("PMS")
def login_user():
	username_info=username.get()
	password_info=password.get()

	file=open(username_info+".txt","w")
	file.write(username_info+"\n")
	file.write(password_info+"\n")
	file.close()

	l=Label(screen1,text="Login Sucessful",fg="green",font=("calibri",11))
	l.place(x=200,y=200)

def register_user():
	name_info=name.get()
	reg_info=reg.get()
	hostel_info=hostel.get()
	gender_info=var.get()
	mobile_info=mobile.get()
	email_info=email.get()

	file=open("new user.txt","w")
	file.write(name_info+"\n")
	file.write(reg_info+"\n")
	file.write(hostel_info+"\n")
	file.write(gender_info+"\n")
	file.write(mobile_info+"\n")
	file.write(email_info+"\n")
	file.close()

	l=Label(screen2,text="Submitted Sucessful",fg="green",font=("calibri",11))
	l.place(x=200,y=400)


def parking_user():
	reg_info=reg.get()
	c1_info=c1.get()
	c2_info=c2.get()
	price_info=price.get()

	file=open("parking.txt","w")
	file.write(reg_info+"\n")
	file.write(c1_info+"\n")
	file.write(c2_info+"\n")
	file.write(price_info+"\n")
	file.close()


	l=Label(screen3,text="Ordered Sucessful",fg="green",font=("calibri",11))
	l.place(x=200,y=250)


def login():
	global screen1
	screen1=Toplevel(screen)
	screen1.title("Login Page")
	screen1.geometry("500x500")
	global username
	global password


	
	l1=Label(screen1,text="Username*",font=("bold",10))
	l1.place(x=100,y=50)
	l2=Label(screen1,text="Password*",font=("bold",10))
	l2.place(x=100,y=100)

	username=StringVar()
	password=StringVar()
	e1=Entry(screen1,textvariable=username)
	e1.place(x=200,y=50)
	e2=Entry(screen1,textvariable=password)
	e2.place(x=200,y=100)
	b=Button(screen1,text="login now",command=login_user,font=("bold",10),padx=30,pady=5,bg="blue")
	b.place(x=200,y=150)
	b1=Button(screen1,text="New User",font=("bold",10),command=register,padx=30,pady=5,bg="blue")
	b1.place(x=370,y=150)

def register():
	global screen2
	screen2=Toplevel(screen)
	screen2.title("Register")
	screen2.geometry("500x500")

	global name
	global reg
	global hostel
	global var
	global mobile
	global email

	lb1=Label(screen2,text="Name",font=("bold",10))
	lb1.place(x=100,y=50)
	lb2=Label(screen2,text="Reg.No",font=("bold",10))
	lb2.place(x=100,y=100)
	lb3=Label(screen2,text="Hostel/Block",font=("bold",10))
	lb3.place(x=100,y=150)
	lb4=Label(screen2,text="Gender",font=("bold",10))
	lb4.place(x=100,y=200)
	lb5=Label(screen2,text="Mobile.No",font=("bold",10))
	lb5.place(x=100,y=250)
	lb6=Label(screen2,text="Email.Id",font=("bold",10))
	lb6.place(x=100,y=300)

	name=StringVar()
	reg=StringVar()
	hostel=StringVar()
	mobile=StringVar()
	email=StringVar()
	var=StringVar()

	e1=Entry(screen2,textvariable=name)
	e1.place(x=200,y=50)
	e2=Entry(screen2,textvariable=reg)
	e2.place(x=200,y=100)
	e3=Entry(screen2,textvariable=hostel)
	e3.place(x=200,y=150)
	r1=Radiobutton(screen2,text="Male",font=("bold",10),variable=var,value=1)
	r1.place(x=195,y=200)
	r2=Radiobutton(screen2,text="Female",font=("bold",10),variable=var,value=2)
	r2.place(x=265,y=200)
	e5=Entry(screen2,textvariable=mobile)
	e5.place(x=200,y=250)
	e6=Entry(screen2,textvariable=email)
	e6.place(x=200,y=300)
	b=Button(screen2,text="Submit",command=register_user,padx=40,pady=5,bg="blue")
	b.place(x=200,y=350)

def parking():
	global screen3
	screen3=Toplevel(screen)
	screen3.title("Parking Request")
	screen3.geometry("500x500")
	global reg
	global c1
	global c2
	global price

	l1=Label(screen3,text="Reg.No",font=("bold",10))
	l1.place(x=100,y=50)
	l2=Label(screen3,text="Parking Block",font=("bold",10))
	l2.place(x=100,y=100)
	l3=Label(screen3,text="Price",font=("bold",10))
	l3.place(x=100,y=150)

	reg=StringVar()
	c1=StringVar()
	c2=StringVar()
	price=StringVar()

	e1=Entry(screen3,textvariable=reg)
	e1.place(x=200,y=50)
	cb=Checkbutton(screen3,text="A",font=("bold",10),offvalue=0,onvalue=1,variable=c1)
	cb.place(x=195,y=100)
	cb2=Checkbutton(screen3,text="B",font=("bold",10),offvalue=0,onvalue=1,variable=c2)
	cb2.place(x=290,y=100)
	e1=Entry(screen3,textvariable=price)
	e1.place(x=200,y=150)
	b=Button(screen3,text="Order",command=parking_user,font=("bold",10),padx=40,pady=5,bg="blue")
	b.place(x=200,y=200)
	
screen.geometry("500x500")
b=Button(screen,text="Login",command=login,font=("bold",10),padx=10,pady=5,bg="blue") 
b.place(x=80,y=50)
b2=Button(screen,text="New User",command=register,font=("bold",10),padx=10,pady=5,bg="blue")
b2.place(x=200,y=50)
b3=Button(screen,text="Available parking",command=parking,font=("bold",10),padx=10,pady=5,bg="blue")
b3.place(x=340,y=50)
screen.mainloop()





	
