import flet
from flet import Page, Container, Row, Text, padding


def main(page: Page):
    page.title = "Row lesson"
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_width = 400
    page.window_height = 800
    page.theme_mode = 'light'
    # page.scroll = "auto"

    row = Row(
        controls=[
            Container(
                content=Text(value="First child", color="white"),
                width=100, height=100,
                bgcolor="#26474e"
            ),

            Container(
                content=Text(value="Second child", color="white"),
                width=100, height=100,
                bgcolor="#26474e"
            ),

            Container(
                content=Text(value="Third child", color="white"),
                width=100, height=100,
                bgcolor="#26474e"
            ),

            Container(
                content=Text(value="Fourth child", color="white"),
                width=100, height=100,
                bgcolor="#26474e"
            ),

            Container(
                content=Text(value="Fifth child", color="white"),
                width=100, height=100,
                bgcolor="#26474e"
            ),

            Container(
                content=Text(value="Sixth child", color="white"),
                width=100, height=100,
                bgcolor="#26474e"
            )

        ],
        # wrap=True,
        scroll='always',
        spacing=3,
        run_spacing=3,
        # alignment='spaceEvenly'

    )

    rowContainer = con
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)

