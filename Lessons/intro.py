import flet
from flet import Page, Text


def main(page: Page):
    page.title = "introduction app"
    page.bgcolor = "#176d95"
    page.padding = flet.padding.only(top=20, bottom=20, left=10, right=10)
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.scroll = 'auto'
    page.add(Text(value="This is a good tutorial"))

    for i in range(100):
        t = Text(value="helo world!")
        page.add(t)

    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
