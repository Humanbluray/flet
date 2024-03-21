import flet
from flet import (Page, Container, Tabs, Tab, colors, margin, padding, Text, TextField, Icon, icons)


def main(page: Page):
    page.title = 'tabs tutorial'

    def tab_change(e: flet.ControlEvent):
        print('tab change')
        print(e.data)
        print(e.name)

    tab = Tabs(
        selected_index=1,
        animation_duration=1000,
        on_change=tab_change,
        width=300,
        height=500,
        expand=True,
        tabs=[
            Tab(
                text='tab1',
                icon=icons.GRADE_OUTLINED,
                # tab_content=Icon(name=icons.PERSON_2),
                content=Text(value='this is tab1', color="black"),
            ),
            Tab(
                text='tab2',
                icon=icons.FLIP_CAMERA_ANDROID,
                # tab_content=Icon(name=icons.DATASET),
                content=Text(value='This is tab 2', color="black")
            ),
            Tab(
                text='tab3',
                icon=icons.HEART_BROKEN_SHARP,
                # tab_content=Icon(name=icons.DARK_MODE),
                content=Text(value='This is tab 3', color="black")
            )
        ]
    )

    page.add(tab)
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
