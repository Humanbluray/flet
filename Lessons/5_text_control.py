import flet
from flet import Text, Page, Column, colors


def main(page: Page):

    page.title = "text controls"
    page.bgcolor = colors.ORANGE_300
    page.window_width = 400
    page.window_height = 750

    c = Column(
        controls=[
            Text(value="Hello world! dfdfgh dffdf  dfdf sd ds d sdsde  efe",
                 size=40,
                 # bgcolor=colors.BLUE_GREY_500,
                 # selectable=True,
                 # weight="bold",
                 italic=True,
                 # max_lines=1,
                 # overflow="faded",
                 text_align="left",
                 style="displayLarge"

                 ),

            Text(value="Speed coding", style="displayMedium")
        ]
    )
    page.add(c)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)