from tkinter import*
from main_screen import*


def Insert():
	global root1
	root1=Toplevel()
	root1.title("Register form")
	root1.geometry("750x650")
	root1.config(bg="red")

	global Name_var, Gender_var, DOB_var, Address_var, Phone_number_var,Email_var
	global name_entry, gender_entry, DOB_entry, address_entry, phone_number_entry,email_entry
	Name_var=  StringVar()
	Gender_var= StringVar()
	DOB_var= StringVar()
	Address_var=StringVar()
	Phone_number_var=StringVar()
	Email_var=StringVar()

	Label (root1,  text="Fill Your Details", font=("times new roman ", 14, "bold")).pack()
	Label (root1,  text="  ").pack()
	
	Label (root1,  text="Name * ", font=("times new roman ", 14, "bold")).pack()
	name_entry=Entry(root1, textvariable=Name_var)
	name_entry.pack()

	Label (root1, text="Gender * ", font=("times new roman",14,"bold")).pack()
	gender_entry=Entry(root1, textvariable=Gender_var)
	gender_entry.pack()

	Label (root1, text="DoB * ",font=("times new roman", 14, "bold")).pack()
	DOB_entry=Entry(root1, textvariable=DOB_var)
	DOB_entry.pack()

	Label (root1, text="Address * ", font=("times new roman",14,"bold")).pack()
	address_entry=Entry(root1, textvariable=Address_var)
	address_entry.pack()

	Label (root1, text="Email * ", font=("times new roman",14,"bold")).pack()
	email_entry=Entry(root1, textvariable=Email_var)
	email_entry.pack()

	Label (root1, text="phone_Number * ",font=("times new roman",14,"bold")).pack()
	phone_number_entry=Entry(root1, textvariable=Phone_number_var)
	phone_number_entry.pack()

	Label(root1, text = " ", font=("times new roman", 13,"bold")).pack()
	Button(root1, text = "Enter ", width = 11, height = 1, command = register_details).pack()

def register_details():
	name_info=Name_var.get()
	gender_info=Gender_var.get()
	DOB_info=DOB_var.get()
	address_info=Address_var.get()
	phone_number_info=Phone_number_var.get()
	email_info=Email_var.get()
	

	file=open('Database.txt ', 'a')
	file.write("Name"+name_info+"\t""Gender"+gender_info+"\t""DOB"+DOB_info+"\t""Email"+email_info+"\t""Phone_number"+phone_number_info+"\t""Address"+address_info+"\n"+"\n")
	#file.write(gender_info+ "\n ")
	#file.write(DOB_info+ " \n ")
	#file.write(phone_number_info + "\n")
	file.close()

	name_entry.delete(0, END)
	gender_entry.delete(0,END)
	DOB_entry.delete(0,END)
	address_entry.delete(0,END)
	phone_number_entry.delete(0,END)
	email_entry.delete(0,END)

	Label(root1, text = "Your details is registered, Good luck " , font = (" times new roman ",14 , "bold" )).pack()

	root1.mainloop()
#font is used several times , since we are refering the word format style, 
#bold= making our data and variabble bold
#file.close(), mean closing our details
#var=variable we have assigned and created
#M Nar Bdr Kharka,
#12190065
#