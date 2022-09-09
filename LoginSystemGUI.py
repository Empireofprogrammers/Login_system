from tkinter import * 
from tkinter import messagebox
import Users
import time
import PasswordGenerator

#Setting 
Main_screen = Tk()
User = Users.UserModel()
Main_screen.title("Log in screen")#seeting the title of the log in screen
Main_screen.geometry("650x300")# settting the defalt size of the log in screen

#Functions Only for gui Not reusable no changes suggested

def CloseMainWindow():
    time.sleep(2)
    Main_screen.destroy()
    
def AdminView():
    AllUsersWindow = Tk()
    AllUsersDetails = User.GetUsersDetails()
    Label(AllUsersWindow,text="These all the Users Details Execpt Password feild:- ",font=("Bold", 20)).pack()
    Label(AllUsersWindow,text="User Name  /   Password    /    Dob",font=("Bold", 20)).pack()
    for user in AllUsersDetails:
        Label(AllUsersWindow,text=user).pack()

def CloseLoginScreen():
    LoginValid.destroy()
def Login():
    try :
        User_valid = User.ValidateCredentials(User_name.get(), Password.get())
        
        if User_valid == True:
            global LoginValid
            LoginValid = Tk()
            LoginValid.title("Welcome")
            UserDetails = User.GetUserDetailByUserName(User_name.get())
            Label(LoginValid,text="Hi "+UserDetails[0],font=("Bold", 20)).pack()
            Label(LoginValid,text="Your Current Account is set as:- "+UserDetails[1],font=("Simple", 10)).pack()
            Label(LoginValid,text="Your Date of Birth is set as:- "+UserDetails[2],font=("Simple", 10)).pack()
            Button(LoginValid,text="Close",command=CloseLoginScreen).pack()
            if UserDetails[1] == "Admin":
                Button(LoginValid,text="View All Users",command=AdminView).pack()
        else:
            messagebox.showerror("Account Error", "Sorry you don't have an account")
    except:
            messagebox.showerror("Account Error", "Sorry plz complete the details")

def PlaceGenPassword():
    Register_Password.insert(0,GeneratedPassword)
    GeneratePasswordWindowWidget.destroy()
def DisplayGeneratedPassword():
    global GeneratedPassword
    Password = PasswordGenerator.PasswordGenerator()
    try:
        GeneratedPassword = Password.GeneratePassword(UpperCharacter.get(),LowerCharacter.get(),Numbers.get(),SpeicalCharacter.get())
        Label(GeneratePasswordWindowWidget,text="You can use this Password")
        Button(GeneratePasswordWindowWidget,text=GeneratedPassword,command=PlaceGenPassword).pack()
    except Exception:
        messagebox.showerror("Incorrect Data", "The data provided to generate password in not valid")
    
def GeneratePasswordWindow():
    global GeneratePasswordWindowWidget
    global UpperCharacter
    global LowerCharacter
    global Numbers
    global SpeicalCharacter
    
    GeneratePasswordWindowWidget = Tk()
    GeneratePasswordWindowWidget.title("Generate Password Window")
    
    Label(GeneratePasswordWindowWidget,text="How many upper case characters:- ").pack()
    UpperCharacter = Entry(GeneratePasswordWindowWidget)
    UpperCharacter.pack()
    
    Label(GeneratePasswordWindowWidget,text="How many lower case characters:- ").pack()
    LowerCharacter = Entry(GeneratePasswordWindowWidget)
    LowerCharacter.pack()
    
    Label(GeneratePasswordWindowWidget,text="How many Numbers:- ").pack()
    Numbers = Entry(GeneratePasswordWindowWidget)
    Numbers.pack()
    
    Label(GeneratePasswordWindowWidget,text="How many Speical Characters:- ").pack()
    SpeicalCharacter = Entry(GeneratePasswordWindowWidget)
    SpeicalCharacter.pack()
    
    Button(GeneratePasswordWindowWidget,text="Submit",command=DisplayGeneratedPassword).pack()

def Register():
    User.MakeAccount(Register_user_name.get(),Register_Password.get(),Dob.get())
    Register_window.destroy()
def RegisterNowWindow():
    global Register_user_name
    global Register_Password
    global Dob
    global Register_window
    
    Register_window = Tk()
    Register_window.geometry("600x350")# settting the defalt size of Register window
    
    Label(Register_window,text="Enter the following Details to Register",font=("Bold", 20)).pack()
    
    Label(Register_window,text="User Name:- ").pack()
    Register_user_name = Entry(Register_window)#Making the entry box for getting the User name for log in
    Register_user_name.pack()
    
    Label(Register_window,text="Password:- ").pack()
    Register_Password = Entry(Register_window,show="#")#Making the entry box for getting the User Password for log in and insted of showing the Entry password showing it with an #
    Register_Password.pack()
    
    Label(Register_window,text="Dob:- ").pack()
    Dob = Entry(Register_window)#Making the entry box for getting the User Password for log in and insted of showing the Entry password showing it with an #
    Dob.pack()
    
    Button(Register_window,text="Generate Password",command=GeneratePasswordWindow).pack()
    Button(Register_window,text="Submit",command=Register).pack()


#Button and Labels
Label(Main_screen,text="Welcome To Empire of programmers login system",font=("Bold", 20)).pack()

Label(Main_screen,text="User Name:- ").pack()
User_name = Entry(Main_screen)#Making the entry box for getting the User name for log in
User_name.pack()

Label(Main_screen,text="Password:- ").pack()
Password = Entry(Main_screen,show="#")#Making the entry box for getting the User Password for log in and insted of showing the Entry password showing it with an #
Password.pack()

Button(Main_screen,text="Log in", bg="light blue",command=Login).place(x=140,y=200)
Label(Main_screen,text=" Not have an Account then").place(x=250,y=200)
Button(Main_screen,text="Register Now", bg="light green",command=RegisterNowWindow).place(x=445,y=200)
#Button(Main_screen,text="Register Now", bg="light green",command=RegisterNowWindow).place(x=445,y=200)
Button(Main_screen,text="Exit", bg="red",command=CloseMainWindow).place(x=300,y=250)
Main_screen.mainloop()
