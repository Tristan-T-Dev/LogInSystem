import ast
from tkinter import *
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg='#fff')
        self.root.resizable(False, False)

        self.create_login_ui()

    def create_login_ui(self):
        img = PhotoImage(file='login.png')
        Label(self.root, image=img, border=0, bg='white').place(x=120, y=50)
        self.root.img = img  # To prevent garbage collection of the image

        frame = Frame(self.root, width=350, height=350, bg='#fff')
        frame.place(x=480, y=70)

        heading = Label(frame, text='Log In', fg="#57a1f8", bg='white', font=('Monospace', 23, 'bold'))
        heading.place(x=100, y=5)

        self.user_entry = self.create_entry(frame, 'Username', 30, 80)
        self.password_entry = self.create_entry(frame, 'Password', 30, 150)

        Button(frame, width=39, pady=7, text='Log In', bg='#57a1f8', fg='white', border=0, command=self.signin).place(x=35, y=204)

        label = Label(frame, text="I don't have an Account", fg='black', bg='white', font=('monospace', 9))
        label.place(x=75, y=257)

        Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.signup_window).place(x=220, y=257)

    def create_entry(self, frame, placeholder, x, y):
        def on_enter(e):
            entry.delete(0, 'end')

        def on_leave(e):
            if entry.get() == "":
                entry.insert(0, placeholder)

        entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Monospace', 11))
        entry.place(x=x, y=y)
        entry.insert(0, placeholder)
        entry.bind('<FocusIn>', on_enter)
        entry.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=x - 5, y=y + 27)

        return entry

    def signin(self):
        username = self.user_entry.get()
        pass_code = self.password_entry.get()

        try:
            with open('datasheet.txt', 'r') as file:
                data = file.read()
                users = ast.literal_eval(data)

            if username in users.keys() and pass_code == users[username]:
                self.open_lobby()
            else:
                messagebox.showerror('Invalid', 'Invalid username or password!')
        except FileNotFoundError:
            messagebox.showerror('Error', 'No user data found. Please sign up first.')

    def open_lobby(self):
        screen = Toplevel(self.root)
        screen.title('Lobby')
        screen.geometry('925x500+300+200')
        screen.config(bg='#fff')
        Label(screen, text="Welcome, User!", fg='black', bg='white', font=('Monospace', 16)).pack()
        screen.mainloop()

    def signup_window(self):
        SignupApp(self.root)


class SignupApp:
    def __init__(self, root):
        self.window = Toplevel(root)
        self.window.title("Sign Up")
        self.window.geometry('925x500+300+200')
        self.window.configure(bg='#fff')
        self.window.resizable(False, False)

        self.create_signup_ui()

    def create_signup_ui(self):
        img = PhotoImage(file='login.png')
        Label(self.window, image=img, border=0, bg='white').place(x=120, y=50)
        self.window.img = img

        frame = Frame(self.window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=50)

        heading = Label(frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Monospace', 23, 'bold'))
        heading.place(x=100, y=5)

        self.user_entry = self.create_entry(frame, 'Username', 30, 80)
        self.password_entry = self.create_entry(frame, 'Password', 30, 150)
        self.confirm_password_entry = self.create_entry(frame, 'Confirm Password', 30, 220)

        Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', command=self.signup, border=0).place(x=35, y=280)

        label = Label(frame, text='I have an Account', fg='black', bg='white', font=('monospace', 9))
        label.place(x=90, y=340)

        Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.window.destroy).place(x=200, y=340)

    def create_entry(self, frame, placeholder, x, y):
        def on_enter(e):
            entry.delete(0, 'end')

        def on_leave(e):
            if entry.get() == "":
                entry.insert(0, placeholder)

        entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Monospace', 11))
        entry.place(x=x, y=y)
        entry.insert(0, placeholder)
        entry.bind('<FocusIn>', on_enter)
        entry.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=x - 5, y=y + 27)

        return entry

    def signup(self):
        username = self.user_entry.get()
        passcode = self.password_entry.get()
        con_code = self.confirm_password_entry.get()

        if username == 'Username' or passcode == 'Password' or con_code == 'Confirm Password':
            messagebox.showerror('Error', 'All fields are required')
        elif passcode != con_code:
            messagebox.showerror('Error', 'Passwords do not match')
        else:
            try:
                with open('datasheet.txt', 'r+') as file:
                    data = file.read()
                    users = ast.literal_eval(data)

                    users.update({username: passcode})
                    file.seek(0)
                    file.truncate()
                    file.write(str(users))

                messagebox.showinfo('Signup', 'Successfully signed up')
            except FileNotFoundError:
                with open('datasheet.txt', 'w') as file:
                    file.write(str({username: passcode}))
                messagebox.showinfo('Signup', 'Successfully signed up')

if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
