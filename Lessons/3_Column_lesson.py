import flet
from flet import Page, Container, Column, Text, border, padding


def main(page: Page):
    page.title = "Row Container"
    page.vertical_alignment = 'center'
    page.window_width = 350
    page.window_height = 700

    columnDisposition = Column(
        controls=[
            Container(
                content=Text(value="first child", color='white', size=20),
                bgcolor="#FFC600",
                height=70, width=350,
                border_radius=20,
                padding=padding.only(bottom=10, top=10, left=20, right=20)
            ),

            Container(
                content=Text(value="second child", color='white', size=20),
                bgcolor="#FFC600",
                height=70, width=350,
                border_radius=20,
                padding=padding.only(bottom=10, top=10, left=20, right=20)
            ),

            Container(
                content=Text(value="third child", color='white', size=20),
                bgcolor="#FFC600",
                height=70, width=350,
                border_radius=20,
                padding=padding.only(bottom=10, top=10, left=20, right=20)
            ),

            Container(
                content=Text(value="fourth child", color='white', size=20),
                bgcolor="#FFC600",
                height=70, width=350,
                border_radius=20,
                padding=padding.only(bottom=10, top=10, left=20, right=20)
            ),

            Container(
                content=Text(value="first child", color='white', size=20),
                bgcolor="#FFC600",
                height=20, width=350,
                border_radius=20,
                padding=padding.only(bottom=10, top=10, left=20, right=20)
            ),

            Container(
                content=Text(value="first child", color='white', size=20),
                bgcolor="#FFC600",
                height=100, width=100,
                border_radius=20,
                padding=padding.only(bottom=10, top=10, left=20, right=20)
            ),

            Container(
                content=Text(value="first child", color='white', size=20),
                bgcolor="#FFC600",
                height=100, width=100,
                border_radius=20,
                padding=padding.only(bottom=10, top=10, left=20, right=20)
            ),

            Container(
                content=Text(value="first child", color='white', size=20),
                bgcolor="#FFC600",
                height=100, width=100,
                border_radius=20,
                padding=padding.only(bottom=10, top=10, left=20, right=20)
            )

        ],
        # wrap=True,
        scroll='auto',
        spacing=5,
        run_spacing=5,
        alignment='center'
        # alignment='spaceEvenly'
    )
    page.add(columnDisposition)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)