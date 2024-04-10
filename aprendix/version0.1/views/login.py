import flet as ft

class Login(ft.UserControl):
	"""docstring for Login"""
	def __init__(self, page):
		super().__init__()
		self.page = page
		print(self.page.client_storage.get("colort")+'vlas')

	#main Container
	def MainContainer(self):
		self.main = ft.Container(
			width=350,
			height=640,
			bgcolor='black',
			border_radius=35,
			padding=8,
			)
		self.main_col = ft.Column()

		self.green_container = ft.Container(
			width=self.main.width,
			height=self.main.height*0.45,
			border_radius=30,
			gradient=ft.LinearGradient(
					begin=ft.alignment.top_left,
					end=ft.alignment.bottom_right,
					colors=['#0f766e', '#064e3b'],
				)
			)

		self.inner_green_container = ft.Container(
			width = self.green_container.width,
			height= self.green_container.height,
			content=ft.Row(
				spacing=0,
				controls=[
					ft.Column(
						expand=4,
						controls=[
							ft.Container(
								padding=20,
								expand=True,
								content=ft.Row(
									controls=[
									ft.Column(
										controls=[
											ft.Text('Bienvenido a la página principal',
												size=18,
												color='white70'
												),
											ft.Text('Linea divisoria',
												size=16,
												weight='bold'
												),
											ft.Container(
												on_click= lambda _: self.page.go('/home'),
												content=ft.Text('Goto home', size=25, color='yellow')
												),
										]
										)
									]
									)
								)
						],
						)
					]
				)
			)
		self.green_container.content=self.inner_green_container

		self.main_col.controls.append(self.green_container)
		self.main.content= self.main_col
		return self.main

	def build(self):

		return ft.Column(controls=[self.MainContainer(),])