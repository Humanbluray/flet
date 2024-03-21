import flet
from flet import (Page, Text, TextField, ElevatedButton, Container,
                  Column, colors, icons, padding, alignment, Row, Icon)

import connection

def main(page: Page):
    page.title = "project with Sqlite"
    page.bgcolor = colors.BLUE_GREY_100

    username = flet.Ref[TextField]()
    email = flet.Ref[TextField]()
    password = flet.Ref[TextField]()
    telephone = flet.Ref[TextField]()

    def submit(e):
        connection.new_user(username.current.value, telephone.current.value,
                            email.current.value, password.current.value)

        for widget in (username, email, password, telephone):
            widget.current.value = ""

        page.update()

    c = Container(
        padding=padding.all(20),
        alignment=alignment.center,
        content=Column(
            horizontal_alignment='center',
            width=500,
            controls=[
                Container(
                    content=Text(
                        value="sqlite3 project",
                        size=20,
                        color=colors.BLACK87),
                    padding=padding.only(bottom=10)
                    ),

                TextField(ref=username,
                          prefix_icon=icons.PERSON, hint_text="username",
                          focused_border_color=colors.DEEP_ORANGE,
                          border_radius=20),

                TextField(ref=telephone,
                          prefix_icon=icons.PHONE_ANDROID, hint_text="Telephone",
                          focused_border_color=colors.DEEP_ORANGE,
                          prefix=Text(value="+237 "), max_length=9,
                          border_radius=20),

                TextField(ref=email, hint_text="E-mail",
                          prefix_icon=icons.MAIL,
                          focused_border_color=colors.DEEP_ORANGE,
                          border_radius=20),

                TextField(ref=password, hint_text="password",
                          password=True, can_reveal_password=True,
                          prefix_icon=icons.PASSWORD,
                          focused_border_color=colors.DEEP_ORANGE,
                          border_radius=20),

                ElevatedButton(
                    on_click=submit,
                    height=50, bgcolor=colors.DEEP_ORANGE, color=colors.WHITE, width=150,
                    content=Container(
                        alignment=alignment.center,
                        content=Row(
                            controls=[
                                Icon(name=icons.PERSON_ADD, color=colors.WHITE),
                                Text(value="Submit", size=18),
                            ],
                            alignment="spaceBetween"
                        )
                    )
                )
            ]
        )
    )

    page.add(c)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
