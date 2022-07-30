from tkinter import *
from functools import partial


#window
LoginWindow = Tk()  
LoginWindow.geometry('500x200')  
LoginWindow.title('DoctorUI - Log In')
def nextstep(username, password):
    import PatientType

#username label and text entry box
usernameLabel = Label(LoginWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(LoginWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(LoginWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(LoginWindow, textvariable=password, show='*').grid(row=1, column=1)  

nextstep = partial(nextstep, username, password)

#login button
loginButton = Button(LoginWindow, text="Login", command=nextstep).grid(row=20, column=7)  

LoginWindow.mainloop()
