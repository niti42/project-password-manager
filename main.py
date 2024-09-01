from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if (website and email and password):

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                       f"\nPassword: {password} \nIs it ok to save")
        if is_ok:
            with open('user_data.txt', 'a') as f:
                user_data = f"{website} | {email} | {password}\n"
                f.write(user_data)

            # Clear the entry fields after saving
            entry_website.delete(0, END)
            entry_email_username.delete(0, END)
            entry_password.delete(0, END)
            entry_email_username.insert(0, string="nithishkr62@gmail.com")

    else:
        messagebox.showinfo(
            title="Oops!", message="Please don't leave any fields empty")


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
label_website.grid(row=1, column=0, sticky="e")
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
entry_password = Entry(width=21)
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


# # Three input boxes next to their respective labels
# # One button: Generate Password

window.mainloop()
