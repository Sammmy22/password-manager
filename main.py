from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
pass_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
password = Entry(width=21)
email_entry = Entry(width=35)
generate_password = Button(text="Generate Password")
add = Button(text="Add", width=36)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password.grid(column=1, row=3, columnspan=1, sticky="EW")
generate_password.grid(column=2, row=3, columnspan=1, sticky="EW")
add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
