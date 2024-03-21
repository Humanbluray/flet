import flet
from flet import Page
from views import view_handler


def main(page: Page):
    pass

    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(view_handler(page)[page.route])

    page.on_route_change = route_change
    page.go('/')


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP)
