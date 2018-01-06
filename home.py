import tkinter as Tk
from tkinter import messagebox
from user import *
import tkMessageBox


class App(object):
    t = Tk.Text
    user_name_entry = Tk.Text
    password_entry = Tk.Text
    login_username = Tk.Text
    login_password = Tk.Text
    user = User()

    def __init__(self, parent):
        self.var1 = Tk.IntVar()
        self.frame_title = "Emails Repository"
        self.root = parent
        self.root.title(self.frame_title)
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        username = Tk.Label(parent, text="Enter user name",fg='blue')
        username.pack()
        self.login_username = Tk.Entry(parent, bd=3.5)
        self.login_username.pack(padx=15, pady=5)
        password = Tk.Label(parent, text="Enter password", fg='blue')
        password.pack()
        self.login_password = Tk.Entry(parent, bd=3.5, show="*")
        self.login_password.pack(padx=15, pady=10)
        login_btn = Tk.Button(parent, text="Login", fg='green',bg='black', width=15, command=self.login)
        login_btn.pack()
        register_btn = Tk.Button(parent, text="Register", command=self.open_Register_Frame, bg='red',fg='black', width=15)
        register_btn.pack(padx=10,pady=10)
        Tk.Checkbutton(parent, text="Remember me!", variable=self.var1).pack()

    def hide(self):
        self.root.withdraw()

    def open_program_Frame(self):
        self.hide()
        self.program_frame = Tk.Toplevel()
        self.program_frame.geometry("500x220")
        self.program_frame.title(self.frame_title)
        add_btn = Tk.Button(self.program_frame,text="Add new email?",command=self.open_add_new_email_frame)
        add_btn.pack()
        search_btn = Tk.Button(self.program_frame,text="search for email?",command=self.open_search_for_mail_frame)
        search_btn.pack()
        handler = lambda: self.onCloseOtherFrame(self.program_frame)
        logout_btn = Tk.Button(self.program_frame,text="logout",command=handler)
        logout_btn.pack()

    def open_Register_Frame(self):
        self.hide()
        about_team_Frame = Tk.Toplevel()
        about_team_Frame.geometry("500x220")
        about_team_Frame.title("otherFrame")
        userName_label = Tk.Label(about_team_Frame, text="Enter user_name", fg="blue", font=("Helvetica", 16))
        userName_label.pack()
        self.user_name_entry = Tk.Entry(about_team_Frame, bd=5)
        self.user_name_entry.pack(padx=15, pady=5)
        password_label = Tk.Label(about_team_Frame, text="Enter password", fg="blue", font=("Helvetica", 16))
        password_label.pack()
        self.password_entry = Tk.Entry(about_team_Frame, bd=5)
        self.password_entry.pack(padx=15, pady=5)
        handler = lambda: self.onCloseOtherFrame(about_team_Frame)
        btn = Tk.Button(about_team_Frame, text="Save", command=self.save_register_data)
        btn.pack()
        btn = Tk.Button(about_team_Frame, text="Back", command=handler)
        btn.pack()

    def login(self):
        username = self.login_username.get()
        password = self.login_password.get()
        print username
        print password
        print self.var1.get() # 1 if remember me clicked, 0 for not remember me.
        check = self.user.login(username, password)
        if check == "valid":
            if self.var1.get() == 0:
                self.login_username.delete(0, Tk.END)
                self.login_password.delete(0, Tk.END)
            self.open_program_Frame()
        elif check == "Invalid":
            tkMessageBox.showinfo("failed", "login fail, try again!")

    def open_add_new_email_frame(self):
        self.program_frame.withdraw()
        self.new_email_frame = Tk.Toplevel()
        self.new_email_frame.title(self.frame_title)
        self.new_email_frame.geometry("500x220")
        category = Tk.Label(self.new_email_frame,text="Category")
        category.pack()
        self.category = Tk.Entry(self.new_email_frame,)
        self.category.pack()
        user_name = Tk.Label(self.new_email_frame,text="Username")
        user_name.pack()
        self.username = Tk.Entry(self.new_email_frame)
        self.username.pack()
        password = Tk.Label(self.new_email_frame,text="password")
        password.pack()
        self.password = Tk.Entry(self.new_email_frame,show="*")
        self.password.pack()
        submit_btn = Tk.Button(self.new_email_frame,text="Submit",fg="green",width=10,command=self.submit_email)
        submit_btn.pack()
        handler = lambda: self.mine_destroy(self.new_email_frame)
        back_btn = Tk.Button(self.new_email_frame,text="back",width=10,command=handler)
        back_btn.pack()

    def submit_email(self):
        if self.user.add_email(self.category.get(),self.username.get(),self.password.get()):
            tkMessageBox.showinfo("success", "your data has been submitted successfully")
        else:
            tkMessageBox.showinfo("failed", "some Errors occured please try again!")
    def mine_destroy(self,frame):
        frame.destroy()
        self.mine_show()

    def mine_show(self):
        self.program_frame.update()
        self.program_frame.deiconify()

    def open_search_for_mail_frame(self):
        self.program_frame.withdraw()
        self.search_email_frame = Tk.Toplevel()
        self.search_email_frame.title(self.frame_title)
        self.search_email_frame.geometry("500x220")
        handler = lambda: self.mine_destroy(self.search_email_frame)
        back_btn = Tk.Button(self.search_email_frame, text="back", command=handler)
        back_btn.pack()

    def save_register_data(self):
        username = self.user_name_entry.get(0, Tk.END)
        password = self.password_entry.get(0, Tk.END)
        self.user.register(username, password)
        if self.user.save_data():
            tkMessageBox.showinfo("Congratulations", "Your data have been submitted successfully!")
        elif not self.user.save_data():
            tkMessageBox.showinfo("Ops!", "couldn't create file please check program directory permissions.")

    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

    def show(self):
        self.root.update()
        self.root.deiconify()

    def open_login_Frame(self):
        self.hide()
        otherFrame = Tk.Toplevel()
        otherFrame.geometry("300x200")
        otherFrame.title("Login")
        username = Tk.Label(otherFrame, text="Enter user name")
        username.pack()
        self.login_username = Tk.Entry(otherFrame, bd=5)
        self.login_username.pack(padx=15, pady=5)
        password = Tk.Label(otherFrame, text="Enter password")
        password.pack()
        self.login_password = Tk.Entry(otherFrame, bd=5)
        self.login_password.pack(padx=15, pady=10)
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        btn = Tk.Button(otherFrame, text="Back", width=15, command=handler)
        btn.pack()
        btn = Tk.Button(otherFrame, text="Login", fg='green', width=15, command=self.login)
        btn.pack()


root = Tk.Tk()
root.geometry("500x220")
app = App(root)
root.mainloop()
