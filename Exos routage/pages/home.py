from flet import Container, ElevatedButton, Text, UserControl, Column, Row, Icon, icons


class Home(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Container(
            content=Column(
                alignment='center',
                controls=[
                    Text(
                        value="Home page",
                        size=40,
                    ),
                    ElevatedButton(
                        on_click=lambda e: self.page.go('/login'),
                        content=Row(
                            alignment='spaceBetween',
                            controls=[
                                Text(value="Go to Login"),
                                Icon(name=icons.SEND)
                            ]
                        )
                    )
                ]
            )
        )