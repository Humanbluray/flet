from flet import *

textfield_style: dict = {
    "width": 250,
    "height": 50,
    "content_padding": 12,
    "prefix_icon": icons.TASK_ALT_OUTLINED,
    "hint_text": "your task here...",
    "cursor_height": 24
}

first_container_style: dict = {
    "border": border.all(width=1, color=colors.with_opacity(0.5, "white")),
    "height": 70,
    "padding": 15
}

second_container_style: dict = {
    "border": border.only(left=border.BorderSide(width=5, color=colors.RED))
}