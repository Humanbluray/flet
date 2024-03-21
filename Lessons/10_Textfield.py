import flet
from flet import Page, Text, TextField, Container, colors, padding, border, border_radius, icons, Column, Icon


def main(page: Page):
    page.title = 'textfields'
    page.window_width = 350
    page.window_height = 700
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def on_focus(e):
        print(login.value)

    login = TextField(
        label="Login",
        password=False,
        prefix_icon=icons.EMAIL,
        border_radius=20,
        width=300,
        helper_text="enter a valid e-mail",
        color=colors.GREY_900,
        on_focus=on_focus,
        border=border.only(bottom=10)

    )
    password = TextField(
        label="Password",
        password=True,
        prefix_icon=icons.PERSON,
        border_radius=20,
        width=300,
        can_reveal_password=True
        # helper_text="enter a password"
    )

    phone = TextField(
        label="Cellphone numer",
        prefix_icon=icons.PHONE_ANDROID,
        border_radius=20,
        width=300,
        prefix=Text(value="+237 "),
        max_length=9,
        # helper_text="enter a password"
    )

    # icon = Icon(name=icons.ADD_CARD, size=100)

    column = Column(
        controls=[
            login, password, phone
        ]
    )

    page.add(column)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
