import flet
from flet import Image, Page, colors, border, Container


def main(page: Page):
    page.title = 'Image control'
    page.vertical_alignment = 'center'
    page. horizontal_alignment = 'center'
    page.bgcolor = colors.BLUE_GREY

    c = Container(
        content=Image(
            src="ordinateur.jpg",
            scale=0.8
        ),
        border=border.all(width=10, color=colors.RED_600),
        border_radius=25

    )
    page.add(c)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)

