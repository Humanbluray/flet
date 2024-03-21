from flet import (UserControl, Column, Text, Container,
                  ElevatedButton, colors)


class Home(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Container(
            height=800,
            width=300,
            bgcolor=colors.DEEP_ORANGE,
            content=Column(
                controls=[
                    Text(value='Home page', size=16),
                    ElevatedButton(
                        text="go to login page",
                        bgcolor=colors.BLACK87,
                        color=colors.WHITE,
                        on_click=lambda e:self.page.go('/login')
                    )
                ]
            )
        )



