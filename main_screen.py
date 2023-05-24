from tkinter import*
from Insert import*
from Display import*
from Search import*
from Delete import*

def main_screen():
	global root
	root=Tk()
	root.geometry("750x650")
	root.title("Nge Charo")
	root.config(bg="yellow")
	root.title("WELCOME TO FRIENDS MANAGEMENTS SYSTEM")
	Label(text = "Nge Charo " , bg="yellow", height="6", width="320", font=("times new roman", 15)).pack()
	Label(text=" ").pack()
	Button(text = " Insert " , bg="blue", height="5", width="33",font=("times new roman"), command = Insert).pack()
	Label(text=" ").pack()
	Button(text= " Display " , bg ="purple", height="5", width="33",font=("times new roman",), command=Display).pack()
	Label(text=" ").pack()
	Button(text= " Search" , bg ="red", height="5", width="33", font=("times new roman",), command=Search).pack()
	Label(text=" ").pack()
	Button(text=" Delete" , bg ="pink", height="5", width="33",font=("times new roman",) , command=Delete).pack()

	root.mainloop()
	main_screen()


#This is our main program , we are calling everything from here
#config is used in the programs , it act as a object, and also like user object
#geometry, we have attached the dimentions
#pack is used again and again, since it help us to keep our data and variable in order from,
#bg= background , background colour we refers to
# root is as same like screen, we have defined it