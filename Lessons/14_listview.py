import flet
from flet import (Page, Container, ListView, colors,
                  Text, icons, padding, alignment)


def main(page: Page):
    page.title = "listview control"
    page.bgcolor = colors.BLUE_GREY_100
    page.scroll = 'auto'

    lv = flet.Ref[ListView]()

    page.add(
        ListView(
            ref=lv, expand=True,
        )
    )

    for i in range(31):
        lv.current.controls.append(Text(value=f"item {i}"))
        page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
