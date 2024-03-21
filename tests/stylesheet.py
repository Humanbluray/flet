from flet import *

add_style_sheet: dict = {"icon_size": 18, "icon": icons.ADD_ROUNDED}
text_style_sheet: dict ={
    "expand": False,
    "height": 50,
    "width": 250,
    "cursor_height": 24,
    "content_padding": 20,
    "prefix_icon": icons.TASK_ALT_SHARP,
    "border": "underline"

}

todo_item_style: dict = {
    "border": border.only(left=BorderSide(width=7, color=colors.CYAN_700))
}
container_task_style: dict = {
    "border": border.all(1, color=colors.with_opacity(0.5, "black")),
    "padding": 5,
    "height": 50
}
