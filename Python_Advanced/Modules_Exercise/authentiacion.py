from tkinter import Button, Entry
from json import dump, loads

from Python_Advanced.Modules_Exercise.buying_page import display_products
from Python_Advanced.Modules_Exercise.canvas import root, frame
from Python_Advanced.Modules_Exercise.helpers import clean_screen, get_password_hash


def get_user_data():
    info_data = []

    with open("db/users_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        width=10,
        height=2,
        command=register
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        bd=0,
        width=10,
        height=2,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 310, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First Name:")
    frame.create_text(100, 100, text="Last Name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg='green',
        fg='white',
        bd=0,
        width=12,
        height=1,
        command=registration
    )

    frame.create_window(285, 250, window=register_button)


def registration():
    info_dict = {
        "First Name": first_name_box.get(),
        "Last Name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
    }
    print(info_dict)
    if check_registration(info_dict):
        with open('db/users_information.txt', 'a') as users_file:
            info_dict["Password"] = get_password_hash(info_dict["Password"])
            dump(info_dict, users_file)
            users_file.write('\n')
            display_products()


def check_registration(info_dict):
    frame.delete("error")

    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                195,
                300,
                text=f"{key} cannot be empty!",
                fill="red",
                tags="error",
            )
            return False

    users_data = get_user_data()

    for user in users_data:
        if user["Username"] == info_dict["Username"]:
            frame.create_text(
                200,
                300,
                text='Username is already taken!',
                fill='red',
                tags='error'
            )

        return False

    return True


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    frame.create_window(240, 150, window=login_button)


def logging():
    if check_login():
        display_products()

    else:
        frame.create_text(
            200,
            200,
            text="Invalid username or password!",
            fill="red",
            tags="error",
        )


def check_login():
    users_data = get_user_data()
    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())
    for user in users_data:
        current_user_username = user["Username"]
        current_user_password = user["Password"]
        if current_user_username == user_username and current_user_password == user_password:
            return True

    return False


def activate_login_button(event):
    info = [
        username_box.get(),
        password_box.get(),
    ]
    for el in info:
        if not el.strip():
            login_button["state"] = "disabled"
            break
        else:
            login_button["state"] = "normal"


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show='*')

login_button = Button(
    root,
    text="Login",
    bg="blue",
    fg="white",
    bd=0,
    command=logging
)

login_button["state"] = "disabled"

root.bind("<KeyRelease>", activate_login_button)