import flet
from flet import Page, Container, Text, alignment, padding, border


def main(page: Page):
    page.title = "lesson one -- container"
    page.bgcolor = "white"
    page.window_height = 800
    page.window_width = 400

    def hello(e):
        print(e)
        print('this is a container')

    c = Container(
        content=Text(value="Hello this is a container", size=40, color="black"),
        bgcolor="#cde4f9",
        width=300, height=200,
        alignment=alignment.center,
        ink=True,
        on_click=hello,
        padding=padding.only(right=10, left=10, top=10),
        # border=border.all(width=5),
        border=border.only(left=border.BorderSide(width=7, color="#044480")),
        # border_radius=flet.border_radius.only(bottom_left=50, bottom_right=50, top_right=10, top_left=10),
        # on_hover=hello,
        # on_long_press=hello,
        margin=10,
        # margin=margin.only(top=10, bottom=10),
        tooltip="this is a container",

    )
    page.add(c)
    page.update()


if __name__ == "__main__":
    flet.app(target=main, view=flet.FLET_APP)
