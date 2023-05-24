from Display import*
from Insert import*
from Search import*
from main_screen import*

def Delete():
	global root4
	root4=Toplevel()
	root4.title("Delete friends:")
	root4.geometry("750x650")
	Label(root4,text="Remove Friends",font=("times new roman",16, "bold")).pack()
	Label(root4,text=" ").pack()

	Label(root4,text="Enter a name to Delete * ", font=("times new roman",15, "bold")).pack()
	name_entry=Entry(root4)
	name_entry.pack()
	Label(root4,text=" ",).pack()
	Button(root4,text="Delete ",bg ="blue",width=9,height=1).pack()
def delete_fun():
	delete_i=delete_var.get()
	with open("Database.txt",'r+') as n:
		new_n=n.readlines()
		n.seek(0)
		for line in new_n:
			if delete_i not in line:
				n.write(line)
		n.turncate()		


	root4.mainloop()








