from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

def signup():
    username = user.get()  
    passcode = password.get()  
    con_code = con_password.get()  


    # Check for empty fields
    if username == 'Username' or passcode == 'Password' or con_code == 'Confirm Password':
        messagebox.showerror('Error', 'All fields are required')  
    elif passcode != con_code:
        messagebox.showerror('Error', 'Passwords do not match') 
    else:
        try:
            # Attempt to read and update the datasheet file
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: passcode}  
            r.update(dict2)  
            file.truncate(0)  
            file.close()

            file = open('datasheet.txt', 'w')
            file.write(str(r)) 
            messagebox.showinfo('Signup', 'Successfully signed up')  
            file.close()
        except:
            # If file does not exist, create it with an initial entry
            file = open('datasheet.txt', 'w')
            pp = str({username: passcode})
            file.write(pp)
            file.close()

def sign():
    window.destroy()
    


img = PhotoImage(file='login.png')
Label(window,image = img,border=0, bg = 'white').place(x=120,y=50)

frame = Frame(window,width=350,height=390, bg='#fff')
frame.place(x=480,y=50)

heading = Label(frame,text = 'Sign Up',fg="#57a1f8", bg='white',font=('Monospace',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=="":
        user.insert(0,"Username")

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Monospace',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    if password.get()=="":
        password.insert(0,"Password")

password = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Monospace',11))
password.place(x=30,y=150)
password.insert(0, 'Password')
password.bind("<FocusIn>", on_enter)
password.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

def on_enter(e):
    con_password.delete(0,'end')

def on_leave(e):
    if con_password.get()=="":
        con_password.insert(0,"Confirm Password")

con_password = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Monospace',11))
con_password.place(x=30,y=220)
con_password.insert(0, 'Confirm Password')
con_password.bind("<FocusIn>", on_enter)
con_password.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

label=Label(frame,text='I have an Account',fg='black', bg='white', font=('monospace',9))
label.place(x=90,y=340)
Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',command=signup,border=0).place(x=35,y=280)
signin = Button(frame,width=6,text='Sign in', border=0,bg='white',cursor='hand2', fg='#57a1f8',command=sign)
signin.place(x=200,y=340)

window.mainloop()
