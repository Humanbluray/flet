from flet import *


class Todo(UserControl):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def build(self):
        c = Checkbox(value=False)
        b1 = IconButton(icon=icons.DELETE_SWEEP)
        b2 = IconButton(icon=icons.ADD)

        return Column(
            controls=[
                Row(controls=[c, self.text, b2, b1]),
                Divider(height=25, color=colors.GREY_200)
            ]
        )
