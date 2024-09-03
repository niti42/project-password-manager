from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_choice = [choice(letters) for _ in range(randint(8, 10))]
    symbols_choice = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_choice = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_choice + symbols_choice + numbers_choice

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, string=f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Get the data from the entry fields
    website = entry_website.get()
    email = entry_email_username.get()
    password = entry_password.get()

    new_data = {}
    if (website and email and password):
        new_data = {website: {
            "email": email,
            "password": password
        }}

        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save")
        if is_ok:
            try:
                with open('user_data.json', 'r') as json_file:
                    user_data = json.load(json_file)
            except FileNotFoundError:
                with open('user_data.json', 'w') as json_file:
                    json.dump(new_data, fp=json_file, indent=4)
            else:
                user_data.update(new_data)
                with open('user_data.json', 'w') as json_file:
                    json.dump(user_data, fp=json_file, indent=4)
            finally:
                # Clear the entry fields after saving
                entry_website.delete(0, END)
                entry_password.delete(0, END)

    else:
        messagebox.showinfo(
            title="Oops!", message="Please don't leave any fields empty")

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def find_password():
    # grab the text which user entered in user name
    website = entry_website.get()
    # search for this text in the keys of user_data.json
    try:
        with open('user_data.json', 'r') as json_file:
            user_data = json.load(json_file)
    # if json file absent, message box: No Data File Found
    except FileNotFoundError:
        messagebox.showinfo(
            title="Oops!", message="No Data File Found")
    else:
        if credentials := user_data.get(website):
            messagebox.showinfo(
                title="Credentials", message=f"Website: {website}\nEmail: {credentials.get('email')}\nPassword: {credentials.get('password')}")
        else:
            messagebox.showinfo(
                title="Oops!", message=f"No details for the {website} exists")

    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
# (100,100) is the center of the image
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=0, padx=20, pady=20, columnspan=3)

# Labels
# Website Label
label_website = Label(text="Website:", font=("Arial", 9, "normal"))
label_website.grid(row=1, column=0)
# my_label.config(padx=10, pady=5)

# Email/Username Label
label_email_username = Label(
    text="Email/Username:", font=("Arial", 9, "normal"))
label_email_username.grid(row=2, column=0, sticky="e")
label_email_username.config(padx=5, pady=5)

# Password Label:
label_password = Label(text="Password:", font=("Arial", 9, "normal"))
label_password.grid(row=3, column=0, sticky="e")
label_password.config(padx=5, pady=5)

# Entries
# Website entry
entry_website = Entry(width=43)
entry_website.insert(END, string="")
entry_website.grid(row=1, column=1, columnspan=2, sticky="w")


# Email/Username entry
entry_email_username = Entry(width=43)
entry_email_username.insert(0, string="nithishkr62@gmail.com")
entry_email_username.grid(row=2, column=1, columnspan=2, sticky="w")

# Password entry
entry_password = Entry(width=43)
entry_password.insert(END, string="")
entry_password.grid(row=3, column=1, sticky="w")

# Buttons
# Generate Password:
button_generate_password = Button(
    text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=1, columnspan=2, sticky="e")

# Add
button_add = Button(
    text="Add", width=36, command=save)
button_add.grid(row=4, column=1)

# Search
button_search = Button(
    text="Search", width=15, command=find_password)
button_search.grid(row=1, column=2)

window.mainloop()
