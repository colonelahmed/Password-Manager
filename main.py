from  tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))
    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if len(web_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="you've left some fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(), message=f"There are the details entered: \nEmail: {email_entry.get()} "
                                                          f"\nPassword: {password_entry.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{web_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:", bg="white")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Entries
web_entry =  Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "ahmed@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
gen_button = Button(text="Generate Password", bg="white", width=13, command=generate_password)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", bg="white", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()