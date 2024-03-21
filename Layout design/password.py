"""UI DESIGN TUTORIAL"""

# importing libraries
from math import pi
import flet
from flet import *

# list to store controls + main list
CONTROLS = []


def store_controls(function):
    def wrapper(*args, **kwargs):
        reference = function(*args, **kwargs)
        CONTROLS.append(reference)
        return reference
    return wrapper


class Main(UserControl):
    def __init__(self):
        super().__init__()

    @property
    def main_title(self):
        return Row(
            alignment=MainAxisAlignment.START,
            controls=[
                Text(value="Dashboard", size=21, weight="bold"),
            ]
        )

    def main_body(self):
        return Container(
            width=260, height=500, border=border.all(0.5, color=colors.WHITE24),
            border_radius=10,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.main_body_title,
                    Divider(height=25, color="transparent"),
                    self.main_body_card
                ]
            )
        )

    @property
    def main_body_title(self):
        return Container(
            padding=15,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text("1. current card", size=12, weight="bold"),
                    Container(
                        content=Row(
                            alignment=MainAxisAlignment.END,
                            spacing=0,
                            controls=[
                                IconButton(icon=icons.ADD_CIRCLE_ROUNDED, icon_size=14),
                                IconButton(icon=icons.SETTINGS, icon_size=14),

                            ]
                        )
                    )
                ]
            )
        )

    def build(self):
        return Column(
            expand=True,
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.main_title,
                Divider(height=25, color="transparent"),
                self.main_body()
            ]
        )

    @property
    def main_body_card(self):
        return Container()
        pass


def main(page: Page):
    page.theme_mode = 'dark'
    page.horizontal_alignment = 'center'
    page.vertical_alignment ='center'
    page.window_height = 450
    page.window_width = 800

    page.add(
        Container(
            width=300, height=620,
            bgcolor='#1d2630', border_radius=10,
            padding=20,
            content=Main()
        )
    )


if __name__ == '__main__':
    flet.app(target=main)
