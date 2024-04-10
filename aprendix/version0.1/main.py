import flet as ft
from views import lsViews
from controles.jsoncontrol import JsonLectura, JsonGuardar

estado_app = JsonLectura('base/estadoapp.json')

def main(page: ft.Page):
    page.title = "Routes Example"
    estado_app = JsonLectura('base/estadoapp.json')
    page.session.set("estado", estado_app)

    def route_change(route):
        page.views.clear()
        if page.route in lsViews:
            ruta= page.route
            color = page.session.get('estado')['color']
            ls, vw =[], lsViews[ruta](page)
            try:
                ls.append(vw.BannerSup())
            except:
                pass
            try:
                ls.append(vw.Body())
            except:
                pass
            try:
                ls.append(vw.BannerInf())
            except:
                pass
            page.views.append(
                ft.View(route=ruta,bgcolor=f'{color}300',controls=ls)
                )
        else:   
            ruta= '/'
            vw = lsViews[ruta]
            page.views.append(
                ft.View(route='/',controls=[vw(page)])
                )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

#ft.app(target=main)
ft.app(target=main, port=8550, view=ft.WEB_BROWSER)