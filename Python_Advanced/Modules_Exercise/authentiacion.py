from tkinter import Button

from Python_Advanced.Modules_Exercise.canvas import root, frame


def render_entry():
    reg_button = Button(
        root,
        text="Register",
        bg='green',
        fg='white',

        command=register

    )

    login_button = Button(
        root,
        text='Login',
        bg='blue',
        fg='white',

        command=login
    )

    frame.create_window(350, 260, window=reg_button)
    frame.create_window(350, 320, window=login_button)


def register():
    print('Register')


def login():
    print('Login')

