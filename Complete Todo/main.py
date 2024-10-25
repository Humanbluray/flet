import flet as ft

_dark: str = ft.colors.with_opacity(0.5, "white")
_light: str = ft.colors.with_opacity(1, 'black')
todo_item_style_sheet: dict = {"height": 50, "border_radius": 4}


class TodoItem(ft.Container):
    def __init__(self, hero: object, description: str, theme: str)->None:

        if theme == 'dark':
            todo_item_style_sheet['border'] = ft.border.all(1, _dark)
        else:
            todo_item_style_sheet['border'] = ft.border.all(1, _light)

        super().__init__(**todo_item_style_sheet)
        self.hero = hero
        self.description = description

        self.tick = ft.Checkbox(on_change=self.strike)
        self.text = ft.Text(spans=[ft.TextSpan(text=self.description)], size=14)
        self.delete = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINE,
            icon_color=ft.colors.RED_700,
            on_click=self.delete_item
        )

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(controls=[self.tick, self.text]),
                self.delete
            ]
        )

    def strike(self, e):
        if self.tick.value is True:
            self.text.spans[0].style = ft.TextStyle(
                decoration= ft.TextDecoration.LINE_THROUGH, decoration_thickness=2
            )
        else:
            self.text.spans[0].style =  ft.TextStyle()

        self.text.update()

    def delete_item(self, e):
        self.hero.todo_area.controls.remove(self)
        self.hero.item_size()
        self.hero.todo_area.update()


class Hero(ft.Container):
    def __init__(self, page:  ft.Page):
        super().__init__()
        self.page = page

        self.title =  ft.Text("Todo List", size=20, weight= ft.FontWeight.W_800)
        self.toggle =  ft.IconButton(icon_size=18, icon= ft.icons.DARK_MODE_ROUNDED, on_click=self.switch)
        self.item =  ft.TextField(height=50, expand=True, border_color=_dark, cursor_height=24,
                              hint_text="Add you todo item here...", content_padding=15)
        self.add =  ft.IconButton(icon= ft.icons.ADD_ROUNDED, icon_size=18, on_click=self.add_item)

        self.todo_area =  ft.Column(expand=True, spacing=18)
        self.counter =  ft.Text("0 items", italic=True)
        self.content = ft.Column(
            controls=[
                ft. Row(
                    alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[self.title, self.toggle],
                ),
                ft.Divider(height=20),
                ft.Divider(height=20, color="transparent"),
                ft.Text("Add your item below"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[self.item, self.add]
                ),
                ft.Divider(height=20, color="transparent"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[ft.Text("2. list of todo items"), self.counter]
                ),
                self.todo_area
            ]
        )

    def switch(self, e):
        if self.page.theme_mode == 'dark':
            self.page.theme_mode = 'light'
            self.toggle.icon = ft.icons.LIGHT_MODE_ROUNDED
            self.item.border_color = _light

            for item in self.todo_area.controls[:]:
                item.border = ft.border.all(1, _light)

        else:
            self.page.theme_mode = 'dark'
            self.toggle.icon = ft.icons.DARK_MODE_ROUNDED
            self.item.border_color = _dark

            for item in self.todo_area.controls[:]:
                item.border = ft.border.all(1, _dark)

        # self.todo_area.update()
        self.page.update()

    def item_size(self):
        if len(self.todo_area.controls[:]) == 1:
            self.counter.value = "1 item"
        else:
            self.counter.value = f"{len(self.todo_area.controls[:])} items"

        self.counter.update()

    def add_item(self, e):
        if self.item.value != "":
            if self.page.theme_mode == 'dark':
                self.todo_area.controls.append(TodoItem(self, self.item.value, "dark"))
            else:
                self.todo_area.controls.append(TodoItem(self, self.item.value, "light"))

            self.todo_area.update()
            self.item.value = ""
            self.item_size()
            self.item.update()
        else:
            pass


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    theme = ft.Theme()
    page.theme = theme

    hero = Hero(page)
    page.add(hero)
    page.update()



if __name__ == '__main__':
    ft.app(target=main)
