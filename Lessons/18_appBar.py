import flet
from flet import (Page, AppBar, Container, Text, colors, Icon, icons, IconButton)


def main(page: Page):
    page.title = 'appbar control'
    # page.bgcolor = colors.TEAL

    page.appbar = AppBar(
        leading=Icon(
            name=icons.PERSON, size=40
        ),
        color=colors.BLACK87,
        title=Text(
            value='first page'
        ),
        leading_width=100,
        center_title=True,
        bgcolor=colors.TEAL_50,
        elevation=100,
        actions=[
            IconButton(
                icon=icons.INSTALL_MOBILE
            )
        ],
        toolbar_height=100

    )
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
