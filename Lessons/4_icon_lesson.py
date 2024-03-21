import flet
from flet import Page, Container, Row, Column, icons, Icon, colors


def main(page: Page):
    page.title = "Icons"
    page.window_width = 350
    page.window_height = 700
    page.horizontal_alignment = "center"
    page.vertical_alignment = 'center'
    page.bgcolor = 'black'

    c = Column(
        controls=[
            Icon(name="add_a_photo", color=colors.ORANGE_800, size=40,
                 # opacity=0.3,
                 tooltip="camera",
                 )
        ]
    )

    page.add(c)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)