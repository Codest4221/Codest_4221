from tkinter import*
def myClick():
    myLabel = Label(root, text = "look you clicked!!!")
    myLabel.pack()



root = Tk()

#Create button  
myButton = Button(root, text = "Click me", padx= 50 ,pady= 50,command = myClick,fg = "blue",bg="red") 
myButton.pack()



root.mainloop()




#--Mete Bingöl--
