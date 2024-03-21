from flet import View
from pages.login import Login
from pages.home import Home


def view_handler(page):
    return {
        '/': View(
            route='/',
            controls=[
                Home(page)
            ]
        ),

        '/login': View(
            route='/login',
            controls=[
                Login(page)
            ]
        )
    }