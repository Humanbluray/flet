from flet import *


def drop_down_search():
    _object_ = Container(
        width=450,
        height=50,
        bgcolor=colors.WHITE10,
        border_radius=6,
        padding=padding.only(top=15, left=21, bottom=15, right=21),
        clip_behavior=ClipBehavior.HARD_EDGE,
        animate=animation.Animation(400, 'decelerate'),
        content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.START,
            controls=[
                Row(
                    spacing=10,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Icon(
                            name=icons.SEARCH_ROUNDED,
                            size=15, opacity=0.90
                        )
                    ]
                )
            ]
        )
    )
    return _object_


class DropdownSearchBar(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return drop_down_search()


def main(page: Page):
    page.theme_mode = "dark"
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'start'
    page.padding = padding.only(top=50)
    page.add(DropdownSearchBar())
    page.update()


if __name__ == '__main__':
    app(target=main)
