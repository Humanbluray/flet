from flet import *

# style sheet ________________________________________
add_style: dict = dict(bgcolor="blue", color="white", text="Add new")
delete_style: dict = dict(bgcolor="red", color="white", text="Delete")
edit_style: dict = dict(bgcolor="orange", color="white", text="Edit")
title_style: dict = dict(value="CRUD Sample", size=30, weight=FontWeight.W_600)
# End style sheet ____________________________________


class Table(UserControl):
    def __init__(self):
        super().__init__()
        self.title = Text(**title_style)
        self.name = TextField(label="Your name here...")
        self.you_id = TextField(visible=False)
        self.add = ElevatedButton(**add_style, on_click=self.add_data)
        self.delete = ElevatedButton(**delete_style)
        self.edit = ElevatedButton(**edit_style, on_click=self.editandsave)
        self.my_table = DataTable(
            columns=[
                # column of the datatable
                DataColumn(Text("id")),
                DataColumn(Text("name")),
                DataColumn(Text("address")),
                DataColumn(Text("Logo"))
            ],
            # Row of the table
            rows=[]
        )

    def add_data(self, e):
        self.my_table.rows.append(
            DataRow(
                cells=[
                    # for id
                    DataCell(Text(str(len(self.my_table.rows)))),
                    DataCell(Text(self.name.value)),
                    DataCell(Text("Fake Address")),
                    DataCell(Icon(name=icons.ARROW_UPWARD_SHARP, color=colors.GREEN_400))
                ],
                on_select_changed=lambda e: self.edit_index(e.control.cells[0].content.value,
                                                            e.control.cells[1].content.value)
            )
        )
        self.my_table.update()

    def edit_index(self, e, r):
        print("your id is", e)
        print("your name is", r)
        self.name.value = r
        self.you_id.value = e
        self.add.visible = False
        self.delete.visible = True
        self.edit.visible = True
        self.edit.update()
        self.delete.update()
        self.add.update()

    def editandsave(self, e):
        pass

    def build(self):
        return Column(
            controls=[
                self.title,
                self.name,
                Row(
                    controls=[
                        self.add, self.delete, self.edit
                    ]
                ),
                self.my_table
            ]
        )


def main(page: Page):
    page.scroll = "auto"
    table = Table()
    page.add(table)
    page.update()


if __name__ == '__main__':
    app(target=main)
