import flet
from flet import (Page, Card, ControlEvent, Icon, icons, colors, Container, Text)


def main(page: Page):
    page.title = 'card control'
    page.theme_mode = 'light'
    page.update()

    card = Card(
        elevation=10,
        width=200,
        height=200,
        margin=20,
        content=Container(
            bgcolor=colors.DEEP_ORANGE,
            content=Text(
                value='Hello world!'
            )
        )
    )
    page.add(card)


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
