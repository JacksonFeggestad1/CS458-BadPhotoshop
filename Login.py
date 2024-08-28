from tkinter import *
import tkinter.ttk
import LoginAPI as clientauthentication
from tkinter import messagebox
from SecondaryWindow import PersistentSecondaryWindow

class LoginWindow:
    def __init__(self):
        return
    
    def showWindow(self, root):
        self.loginWindow = Toplevel(root, bg="#282828")
        self.loginWindow.withdraw()

        self.loginWindow.wm_iconphoto(False, PhotoImage(file="./icons/lmr.png"))

        self.loginWindow.title("Log in to Account")
        self.loginWindow.geometry("400x180")
        self.loginWindow.resizable(width=False, height=False)

        self.windowHeader = Label(self.loginWindow, text="Please log in with your account credentials below.", font=("Arial", 13), pady=10, bg="#282828", fg="white")

        self.loginFrame = Frame(self.loginWindow, bd=5, bg="#282828")

        self.userLabel = Label(self.loginFrame, text="User Email:", font=("Arial", 10), bg="#282828", fg="white")
        self.userEntry = Entry(self.loginFrame, width=20)

        self.passwordLabel = Label(self.loginFrame, text="Password:", font=("Arial", 10), bg="#282828", fg="white")
        self.passwordEntry = Entry(self.loginFrame, show="*", width=15)

        self.eyeIcon = PhotoImage(file="./icons/view.png")
        self.showPasswordLabel = Label(self.loginFrame, image=self.eyeIcon)
        self.showPasswordButton = Button(self.loginFrame, image=self.eyeIcon, command=self.showPassword)

        self.loginButton = Button(self.loginFrame, text="Log In", command=self.validate_login)

        self.windowHeader.pack()
        self.userLabel.grid(row=0, column=0)
        self.userEntry.grid(row=1, column=0)
        self.passwordLabel.grid(row=2, column=0)
        self.passwordEntry.grid(row=3, column=0)
        self.showPasswordButton.grid(row=3, column=1)
        self.loginButton.grid(row=4, column=0, pady=10)
        self.loginFrame.pack()

        self.loginWindow.deiconify()
        self.loginWindow.grab_set()

    def showPassword(self):
        if self.passwordEntry.cget("show") == "*":
            self.passwordEntry.config(show="")
            self.eyeIcon.config(file="./icons/hide.png")
            self.showPasswordLabel.config(image=self.eyeIcon)
        else:
            self.passwordEntry.config(show="*")
            self.eyeIcon.config(file="./icons/view.png")
            self.showPasswordLabel.config(image=self.eyeIcon)
    
    def getUser(self):
        return self.userEntry.get()
    
    def getPassword(self):
        return self.passwordEntry.get()
    
    def validate_login(self): # This function is called when the login button is pressed and uses the API(esk) to login
        userid = self.getUser()
        password = self.getPassword()

        if clientauthentication.login(userid, password) == 'Login successful':
            loggedIn = True
            print(loggedIn)
            messagebox.showinfo("Login", "Login Successful")
        else:
            messagebox.showerror("Login", "Login Failed")


#self, width, height, title, resizable, background, icon, *args, **kwargs
class LoginWindowNew(PersistentSecondaryWindow):
    def __init__(self, app, *args, **kwargs):
        super().__init__(400, 180, "Log In to Account", False, "#282828", "./icons/lmr.png", *args, **kwargs)
        self.app = app
        self.loadScreenElements()

    def loadScreenElements(self):
        windowHeader = Label(self, text="Please log in with your account credentials below.",
                                  font=("Arial", 13), pady=10, bg="#282828", fg="white")

        loginFrame = Frame(self, bd=5, bg="#282828")

        userLabel = Label(loginFrame, text="User Email:", font=("Arial", 10), bg="#282828", fg="white")
        self.userEntry = Entry(loginFrame, width=20)

        passwordLabel = Label(loginFrame, text="Password:", font=("Arial", 10), bg="#282828", fg="white")
        self.passwordEntry = Entry(loginFrame, show="*", width=15)

        self.eyeIcon = PhotoImage(file="./icons/view.png")
        self.showPasswordLabel = Label(loginFrame, image=self.eyeIcon)
        showPasswordButton = Button(loginFrame, image=self.eyeIcon, command=self.showPassword)

        loginButton = Button(loginFrame, text="Log In", command=self.validate_login)

        windowHeader.pack()
        userLabel.grid(row=0, column=0)
        self.userEntry.grid(row=1, column=0)
        passwordLabel.grid(row=2, column=0)
        self.passwordEntry.grid(row=3, column=0)
        showPasswordButton.grid(row=3, column=1)
        loginButton.grid(row=4, column=0, pady=10)
        loginFrame.pack()
        newUserButton = Button(self, text="New User", command=self.make_user)
        newUserButton.pack()

        self.deiconify()
        self.grab_set()

    def showPassword(self):
        if self.passwordEntry.cget("show") == "*":
            self.passwordEntry.config(show="")
            self.eyeIcon.config(file="./icons/hide.png")
            self.showPasswordLabel.config(image=self.eyeIcon)
        else:
            self.passwordEntry.config(show="*")
            self.eyeIcon.config(file="./icons/view.png")
            self.showPasswordLabel.config(image=self.eyeIcon)

    def getUser(self):
        return self.userEntry.get()

    def getPassword(self):
        return self.passwordEntry.get()

    def validate_login(self):  # This function is called when the login button is pressed and uses the API(esk) to login
        userid = self.getUser()
        password = self.getPassword()

        if clientauthentication.login(userid, password) == 'Login successful':
            self.app.logged_in = True
            print(self.app.logged_in)
            self.app.thread.cancel()
            messagebox.showinfo("Login", "Login Successful")
        else:
            messagebox.showerror("Login", "Login Failed")

    def make_user(self):
        userid = self.getUser()
        password = self.getPassword()

        clientauthentication.new_user(userid, password)