from Insert import*
from Display import*
from main_screen import*

def Search():
	global root3
	root3=Toplevel()
	root3.title("Search")
	root3.geometry("750x650")
	global search_var,search_entry
	search_var=StringVar()

	Label(root3,text="You can search your friends details", font=("times new roman", 15,"bold")).pack()
	Label(root3,text=" ").pack()
	Label(root3,text="Enter a name to search * ",font=("times new roman",11,"bold")).pack()
	search_entry = Entry(root3,textvariable=search_var)
	search_entry.pack()

	Label(root3,text=" ").pack()
	Button(root3,text= "Search ", width=10, height=1,command=check).pack()
	

def check():
	search_info=search_var.get()
	f=open('Database.txt','r')
	fr=f.read()

	if search_info in fr:
		b="yes, we won the happiness!"
		Label(root3,text=b).pack()
	else:
		c="Dont worry , you have another chance, just dont Give up!"
		Label(root3, text=c).pack()
	#root3.mainloop()