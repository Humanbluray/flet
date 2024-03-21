from flet import View
from pages.Login import Login
from pages.Home import Home


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
