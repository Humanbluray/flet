from flet import (Page, ProgressBar, colors, padding, Row, IconButton, border, Switch, Ref,
                  icons, Text, TextField, Container, Column, border_radius, margin, Image,
                  alignment, ElevatedButton, FloatingActionButton, Icon, FilledButton, TextButton,
                  UserControl)


class Login(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Container(
            content=Column(
                controls=[
                    Container(
                        width=350, height=40,
                        content=Text(
                            value="login",
                            size=26,
                            weight="bold",
                            color=colors.BLACK87,
                            text_align="left"
                        )
                    ),
                    Container(
                        width=350, padding=padding.only(top=20, bottom=20),
                        # border=border.all(1),
                        alignment=alignment.center,
                        bgcolor=colors.GREY_100,
                        border_radius=30,
                        # alignment='center',
                        content=Column(
                            controls=[
                                TextField(
                                    label="login",
                                    border_radius=20,
                                    width=250,
                                    prefix_icon=icons.MAIL,
                                    bgcolor=colors.WHITE,
                                    focused_bgcolor=colors.YELLOW_50,
                                    focused_border_color=colors.BLUE_700
                                ),
                                TextField(
                                    label="password",
                                    border_radius=20,
                                    width=250,
                                    password=True,
                                    can_reveal_password=True,
                                    bgcolor=colors.WHITE,
                                    prefix_icon=icons.PASSWORD,
                                    focused_bgcolor=colors.YELLOW_50,
                                    focused_border_color=colors.BLUE_700
                                ),
                                FilledButton(
                                    on_click=lambda e:self.page.go('/'),
                                    width=200,
                                    height=50,
                                    content=Row(
                                        alignment="spaceBetween",
                                        controls=[
                                            Text(value="Sign in", size=16, weight="semi-bold"),
                                            Icon(name=icons.SEND)
                                        ]
                                    )
                                ),
                                Row(
                                    controls=[
                                        TextButton(text="Forgot password ?"),
                                        TextButton(text="Not member? Register")
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )



