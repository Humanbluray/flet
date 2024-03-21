from flet import (UserControl, Column, Text, Container,
                  ElevatedButton, colors)


class Login(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Container(
            height=800,
            width=300,
            bgcolor=colors.BLUE_600,
            content=Column(
                controls=[
                    Text(value='login page', size=16),
                    ElevatedButton(
                        text="Back to homepage",
                        bgcolor=colors.BLACK87,
                        color=colors.WHITE,
                        on_click=lambda e: self.page.go('/')
                    )
                ]
            )
        )



