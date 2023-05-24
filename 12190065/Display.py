from tkinter import*
from Insert import*
from main_screen import*


def Display():
	global root2
	root2=Toplevel()
	root2.title("Informations of friends:")
	root2.geometry("750x650")

	Label(root2, text = "INFORMATIONS OF FRIENDS ", font=("times new roman", 20,"bold")).pack()
	Label(root2, text=" ").pack()
	
	Label(root2, text = "Total no. of friends ", font=("times new roman",  16 , "bold")).pack()
	with open("Database.txt",'r') as f:
		contents=f.read()
		count=contents(count("Name"))
	Label(root2,text=count).pack()
	Label(root2,text=" ").pack()


#++++++++++++++++++++++++++++GRAPH***********************************************

	Label(root2,text="Graph",font=("times new roman",14,"bold")).pack()
	import matplotlib.pyplot as mp
	Label(root2,text="Graph:", font=("times new roman",14,"bold")).pack()
	with open("Database.txt",'r') as f:
		x=f.read()
		count_Male=x.count("Male")
		count_Female=x.count("Female")
	gender=["Male","Female"]
	mp.title("number of males and females pie graph")
	mp.pie(values,labels=gender,autopct='%1.1f%%',shadow =True)
	Label(root2,text="number of Male:",font=("times new roman",14)).pack()
	Label(root2,text=count_Male).pack()
	Label(root2,text="number of Female:",font=("times new roman",14)).pack()
	Label(root2,text=count_Female).pack
	Label(root2,text=p.show()).pack()

	root2.mainloop()

#except Exception as e:
#	print("An error was there , try once more",e)
	
#finally:
#	print("Finally done")
#try block is use for exceptional Handelling, try.....except....finally