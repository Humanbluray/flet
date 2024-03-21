import flet
from flet import (Page, Container, ListView, colors, Icon, icons, Image,
                  Text, icons, padding, alignment, ListTile, IconButton)


def main(page: Page):
    page.title = "listTile control"
    # page.scroll = 'always'

    lv = flet.Ref[ListView]()

    page.add(
        ListView(
            ref=lv,
            expand=True
        )
    )

    for i in range(30):
        lv.current.controls.append(
            ListTile(
                title=Text(value=f"name{i}", size=16, weight="bold"),
                subtitle=Text(value=f"email{i}@mail.com"),
                leading=Icon(name=icons.PERSON),
                trailing=IconButton(icon=icons.ADD_CARD_OUTLINED),
                content_padding=10,
                # selected=True,
                # dense=True,
                # is_three_line=True,
            )
        )
        page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
