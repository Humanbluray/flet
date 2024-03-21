from flet import *
from todo import Todo


class Main(UserControl):
    def __init__(self):
        super().__init__()
        self.textfield = TextField(hint_text="player name", prefix_icon=icons.PERSON_2_ROUNDED)
        self.members = Column()

    def add_clicked(self, e):
        member = Todo(self.textfield.value)
        self.members.controls.append(member)
        self.update()

    def build(self):
        return Container(
            content=Column(
                controls=[
                    Row(
                        controls=[
                            self.textfield,
                            IconButton(icon=icons.ADD, on_click=self.add_clicked)
                        ]
                    ),
                    self.members
                ]
            )
        )


def main(page: Page):
    page.theme_mode = 'light'
    page.add(Container(
        content=Main()
        )
    )


if __name__ == '__main__':
    app(target=main)
