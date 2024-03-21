import flet
from flet import *


class Task(UserControl):
    def __init__(self, input_text):
        super().__init__()
        self.task_view = None
        self.input = input_text
        self.edit_view = None
        self.task_cb = None
        self.edit_tf = None

    def build(self):
        self.task_cb = Checkbox(label=self.input, expand=True)
        self.edit_tf = TextField(value=self.input, expand=True)

        self.task_view = Row(
            controls=[
                self.task_cb,
                IconButton(icon=icons.CREATE_OUTLINED, on_click=None),
                IconButton(icon=icons.DELETE_OUTLINED, on_click=None)
            ]
        )
        self.edit_view = Row(
            visible=True,
            controls=[
                self.edit_tf,
                IconButton(icon=icons.CHECK, on_click=None)
            ]
        )
        return Column(
            controls=[
                self.task_view, self.edit_view
            ]
        )


class ToDo(UserControl):
    def __init__(self):
        super().__init__()
        self.input = None
        self.tasks = None
        self.view = None

    def build(self):
        self.input = TextField(hint_text="Task details", expand=True)
        self.tasks = Column()

        view_header = Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text(value='ToDos', style=TextThemeStyle.HEADLINE_MEDIUM),
                Row(
                    controls=[
                        self.input,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                        self.tasks
                    ]
                )
            ]
        )
        return view_header

    def add_clicked(self, e):
        task = Task(input_text=self.input.value)
        self.tasks.controls.append(task)
        self.update()


def start(page: Page):
    todo = ToDo()
    page.add(todo)


if __name__ == '__main__':
    flet.app(target=start, view=flet.FLET_APP)
