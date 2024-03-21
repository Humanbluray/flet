import flet
from flet import (Page, icons, colors, Column,
                  ElevatedButton, Row, Icon, Text, ButtonStyle, buttons, IconButton,
                  FilledButton, FilledTonalButton, TextButton, OutlinedButton)


def main(page: Page):
    page.window_width = 350
    page.window_height = 750
    page.bgcolor = colors.WHITE
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.title = 'Button control'
    page.scroll = "auto"

    c = Column(
        controls=[
            ElevatedButton(
                # text="Send",
                color="white",
                bgcolor=colors.BLUE_700,
                elevation=10,
                # icon=icons.SEND,
                width=350,
                height=50,
                icon_color=colors.DEEP_ORANGE_700,
                on_hover=lambda e: print("hover"),
                on_click=lambda e: print('click'),
                on_long_press=lambda e: print('long press'),

                content=Row(
                    controls=[
                        Text(value="Envoyer"),
                        Icon(name=icons.SEND),
                    ],
                    alignment="spaceBetween"
                ),
                style=ButtonStyle(shape=buttons.RoundedRectangleBorder(radius=30))
            ),

            FilledButton(text="Filled Button", icon=icons.PERCENT),
            OutlinedButton(text="outlined button", icon=icons.ADD_A_PHOTO),
            FilledTonalButton(text="Filled tonal button", icon=icons.ADD_ALARM),
            TextButton(text="Forgot password ?"),
            IconButton(icon=icons.ACCOUNT_CIRCLE_ROUNDED)
        ]
    )
    page.add(c)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
