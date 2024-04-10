from flet import *

class Home(UserControl):
	"""docstring for Home"""
	def __init__(self, page):
		super().__init__()
		self.page = page

	def build(self):
		return Column(
			controls=[
			Container(
				padding=10,
				bgcolor='blue',
				content=Column([
					Row([
					Container(
						ink=True,
						on_click=lambda e: print("test"),
						content=Row([
							Icon(name="menu",color="white",size=20),
							Text("Promosi",size=15,color="White")
							],spacing=1)
					),
					Container(
						ink=True,
						on_click=lambda e: print("test"),
						content=Row([
							Icon(name="home",color="white",size=20),
							Text("Home",size=15,color="White")
							],spacing=1)
					),
					Container(
						ink=True,
						on_click=lambda e: print("test"),
						content=Row([
							Icon(name="message",color="white",size=20),
							Text("Chat",size=15,color="White")
							],spacing=1)
					),

						],spacing=0,alignment="spaceEvenly"),
					Text('Bienvenidos a la página principal'),
					Container(
						on_click= lambda _: self.page.go('/login'),
						content=Text('Goto login', size=25, color='black')
						),
					Container(
						on_click= lambda _: self.page.go('/home'),
						content=Text('Goto home', size=25, color='yellow')
						),
					Container(
						on_click= lambda _: self.ImprimirDatos(),
						content=Text('Imprimir', size=25, color='yellow')
						),
					],alignment="start")
				)
			]
			)

	def ImprimirDatos(self):
		print(self.page.client_storage.get("colort"))