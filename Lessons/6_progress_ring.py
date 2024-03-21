import flet
from flet import Page, ProgressRing, colors


def main(page: Page):
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.title = 'progress ring'
    page.window_height = 750
    page.window_width = 350

    p = ProgressRing(
        color=colors.ORANGE_600,
        bgcolor=colors.GREY_300
    )

    page.add(p)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
