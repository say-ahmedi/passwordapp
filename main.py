import json
from tkinter import *
from tkinter import messagebox
from passwords import generatePassword
import pyperclip




# ---------------------------- SEARCH INFORMATION AB WEBSITE ------------------------------- #

def search_for_password():
        website = website_entry.get()
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        #search if file exists
        except FileNotFoundError:
            messagebox.showerror('Error', 'File not Found')
        else:
           if website in data:
               reset_data()
               info=data[website]
               password=info['password']
               email=info['email']
               messagebox.showinfo(f"{website}",f'Email:{email}\n'
                                             f'Password:{password}')
           else:
               messagebox.showerror('Error',
                                    "There\'s no data about email and password within website named {}".format(website))

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = generatePassword()
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


#Clearing previous entry texts
def reset_data():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    #NO-NEED-email_entry.delete(0, END)


#Saving data
def save_to_data():
    #Getting the values of the entries
    password = password_entry.get()
    emailuser = email_entry.get()
    website = website_entry.get()
    #creating data to save information about website name
    new_data = {
        website:
            {"emailuser":emailuser,"password":password}
    }

    #check for blank fields
    if len(password) == 0 or len(website) == 0:
        messagebox.showerror("Error", "You left some text entry fields blank, please try again.")
        reset_data()

    #if all fields are filled
    else:
        #messagebox-that will appear when the Data is succesfully saved to the txt file
        is_ok = messagebox.askokcancel("DATA INFO", f"Email: {emailuser} "
                                                  f"\nPassword: {password}\n Is it ok to save?")

        if is_ok:
            #Exceptions to avoid errors
            try:
                with open('data.json', 'r') as file:
                    #Reading old data
                    data=json.load(file)
                    #updating old data with the new data
                    data.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data,file,indent=4)
                    reset_data()
            else:
                with open('data.json', 'w') as data_file:
                    #dumping the data-like uploading file
                    json.dump(data, data_file,indent=4)
                    file.close()
                    print(messagebox.showinfo("SUCCESS", "Successfully saved"))
            finally:
                reset_data()
        else:
            messagebox.showerror("INFO", "Something went wrong,write the information again!")
            reset_data()





# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)




canvas = Canvas(width=200, height=200,)
logo_img = PhotoImage(file='../day29/logo.png')
#settling (*args(x,y positions))
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)





#Creating Website title name and entry for it
website_label=Label(text="Website:",fg="black")
website_label.grid(row=1,column=0)
website_entry=Entry(width=33)
website_entry.grid(row=1,column=1,columnspan=1)

search_btn=Button(text="Search",fg='black',bg='purple',command=search_for_password)
search_btn.config(width=14)
search_btn.grid(row=1,column=2)




#Username and Email
email_label=Label(text="Email/Username:",fg="black")
email_label.grid(row=2,column=0)
email_entry=Entry(width=51)
email_entry.insert(0,"seidahmedrashid@gmail.com")
#Columnspan-Баған Аралығы
"""Columnspan is how many columns would take the given entry or button place on the screen"""
email_entry.grid(row=2,column=1,columnspan=2)




#Password
password_label=Label(text="Password:",fg='black')
password_entry=Entry(width=33)
password_entry.grid(row=3, column=1)
password_label.grid(row=3,column=0)




#Generating Password
generate_button=Button(text="Generate Password",fg='black',command=generate_password)
generate_button.config(width=14)
generate_button.grid(row=3,column=2)
add_button=Button(window,width=43,text="Add",fg="black",command=save_to_data)
add_button.grid(row=4,column=1,columnspan=2)


#executing the process
window.mainloop()