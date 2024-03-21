import flet
from flet import (Page, Text, TextField, colors, icons, ElevatedButton)


def main(page: Page):
    page.title = "control ref tutorial"
    page.bgcolor = colors.BLUE_500
    page.window_width = 400
    page.window_height = 750

    def change_text(e):
        login.current.value = "hello universe"
        page.update()

    firstname = flet.Ref[Text]()
    b = flet.Ref[ElevatedButton]()
    login = flet.Ref[TextField]()

    page.add(
        Text(ref=firstname, value="This is a text"),
        TextField(ref=login, label="login",
                  icon=icons.MAIL_ROUNDED),
        ElevatedButton(ref=b, text="Submit",
                       on_click=change_text,
                       bgcolor=colors.BLACK87,
                       color=colors.WHITE,
                       )
    )



    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
