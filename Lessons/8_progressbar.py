import flet
from flet import Page, ProgressBar, Text, colors
import time


def main(page: Page):
    page.title = "progressbar"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'

    p = ProgressBar(color=colors.RED_500,
                    bgcolor=colors.BLUE_200,
                    width=200,
                    # height=30
                    )
    page.add(p)

    for i in range(101):
        p.value = i*0.01
        time.sleep(0.1)
        page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)