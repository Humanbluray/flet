from flet import *

datas = [
    {'name': 'carlos', 'poste': 'striker', 'age': 24},
    {'name': 'yannick', 'poste': 'goalkeeper', 'age': 22},
    {'name': 'rita', 'poste': 'defender', 'age': 16},
    {'name': 'valérie', 'poste': 'winger', 'age': 19},
    {'name': 'norbert', 'poste': 'left back', 'age': 31},
    {'name': 'philippe', 'poste': 'right back', 'age': 28},
    {'name': 'cyrille', 'poste': 'center back', 'age': 29},
    {'name': 'william', 'poste': 'center back', 'age': 22},
    {'name': 'mike',  'poste': 'central midfielder', 'age': 25},
    {'name': 'olivier', 'poste': 'defensive midfielder', 'age': 30},
    {'name': 'ismael', 'poste': 'goalkeeper', 'age': 24},
    {'name': 'raphael', 'poste': 'striker', 'age': 21},
    {'name': 'leiao', 'poste': 'winger', 'age': 27},
]


class Table(UserControl):
    def __init__(self):
        super().__init__()
        self.search_bar = TextField(
            width=250,
            prefix_icon=icons.SEARCH_SHARP,
            border_radius=15,
            border="underline",
            hint_text="tap here...",
            on_change=self.search
        )

        self.go = ElevatedButton(
            text="Go",
            height=40,
            width=100,
            bgcolor=colors.BLACK87,
            color=colors.DEEP_ORANGE,
            # on_click=self.search
        )
        self.back = ElevatedButton(
            text="Back",
            height=40,
            width=100,
            bgcolor=colors.BLACK87,
            color=colors.DEEP_ORANGE,
            # on_click=self.all_data,
        )
        self.data_not_found = Text("Data not found", size=18, weight=FontWeight.BOLD, visible=False)

        self.table =DataTable(
            columns=[
                DataColumn(Text('nom', size=14, weight=FontWeight.BOLD)),
                DataColumn(Text('poste', size=14, weight=FontWeight.BOLD)),
                DataColumn(Text('age', size=14, weight=FontWeight.BOLD)),
            ],
            rows=[]
        )
        self.add_data()

    def add_data(self):
        for data in datas:
            self.table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(data['name'])),
                        DataCell(Text(data['poste'])),
                        DataCell(Text(data['age'])),
                    ]
                )
            )

    def all_data(self):
        for item in self.table.rows[:]:
            self.table.rows.remove(item)

        for data in datas:
            self.table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(data['name'])),
                        DataCell(Text(data['poste'])),
                        DataCell(Text(data['age'])),
                    ]
                )
            )
        self.table.update()

    def search(self, e):
        search_name = self.search_bar.value
        myfiler = list(filter(lambda x: search_name in x['name'], datas))
        self.table.rows = []

        if search_name != "":
            if len(myfiler) > 0:
                for x in myfiler:
                    self.table.rows.append(
                        DataRow(
                            cells=[
                                DataCell(Text(x['name'])),
                                DataCell(Text(x['poste'])),
                                DataCell(Text(x['age'])),
                            ]
                        )
                    )
                self.data_not_found.visible = False
            else:
                self.data_not_found.visible = True

            self.data_not_found.update()
            self.table.update()
        else:
            self.all_data()

    def build(self):
        return Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Container(
                    alignment=alignment.center_left,
                    bgcolor=colors.BLACK87,
                    padding=padding.only(left=10),
                    width=500,
                    height=70,
                    border_radius=border_radius.only(top_left=15, top_right=15),
                    content=Text('Search Bar', size=20,
                                 color="white", style=TextThemeStyle.LABEL_LARGE)
                ),
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        self.search_bar,
                    ]
                ),
                self.table,
                self.data_not_found
            ]
        )


def main(page: Page):
    page.window_width = 500,
    page.window_height = 700
    page.theme_mode = "light"
    page.scroll = ScrollMode.AUTO
    table = Table()
    page.add(
        table
    )


if __name__ == '__main__':
    app(target=main)
