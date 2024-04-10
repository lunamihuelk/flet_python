import flet as ft

class Cero(ft.UserControl):
	"""docstring for Home"""
	def __init__(self, page):
		super().__init__()
		self.page = page

	def ScreenInicio(self):
		self.main = ft.Container(
			padding=8,
			content=ft.Column(
				controls=[
				ft.Divider(height=100, color='transparent'),
				ft.Row(
					alignment='center',
					height=250,
					controls=[ft.Image(
	                	src="assets/imgs/presplash.png"
	        	    )]
					),
				ft.Divider(height=50, color='transparent'),
				ft.Row(alignment='center',controls=[
					ft.ElevatedButton(
					"Ingresar a Plataforma",
					on_click= lambda _: self.page.go('/ialfa'),
					color="black",
					icon="school",
					icon_color="green400",)]),
				]
				)
			)
		return self.main

	def Body(self):
		return self.ScreenInicio()

	def ImprimirDatos(self):
		print(self.page.client_storage.get("colort"))


