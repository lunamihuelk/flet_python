import flet as ft
from controles.jsoncontrol import JsonLectura, JsonGuardar
import pyrebase
import random
class IAlfa(ft.UserControl):
	gridCursos= ft.Row(scroll=ft.ScrollMode.HIDDEN)
	gridTemas = ft.Row(scroll=ft.ScrollMode.HIDDEN)
	gridCoins = ft.Row(scroll=ft.ScrollMode.HIDDEN)
	gridDesaf = ft.Row(scroll=ft.ScrollMode.HIDDEN)
	"""docstring for Home"""
	def __init__(self, page):
		super().__init__()
		self.page = page
		self.VarNeed()	

	def ToggleButtons(self):
		def widget(texto):
			return ft.Row(alignment='center', controls=[ft.Text(f'{texto}')])

		return ft.Container(padding=4, content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
			controls=[
			ft.Container(width=100, border_radius=4, on_click=lambda e: print("test1"), bgcolor='blue', content=widget('Mi creación')),
			ft.Container(width=100, border_radius=4, on_click=lambda e: print("test2"), bgcolor='blue', content=widget('Aleatorio')),
			ft.Container(width=100, border_radius=4, on_click=lambda e: print("test3"), bgcolor='blue', content=widget('Favoritos')),
			]))

	def SupColecCursos(self, titulo, EsCurso=True):
		curso = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,controls=[
			ft.Container(padding=4,content=
				ft.Text(f'{titulo}', size=16, weight='bold')),
			ft.Row(alignment=ft.MainAxisAlignment.END, controls=[
				ft.IconButton('add',icon_color="black",icon_size=16),
				ft.IconButton('Search',icon_color="black",icon_size=16),
				ft.Container(width=8)
				]),
			])
		tema = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,controls=[
			ft.Container(padding=4,content=
				ft.Text(f'{titulo}', size=16, weight='bold')),
			ft.Row(alignment=ft.MainAxisAlignment.END, controls=[
				ft.IconButton('add',icon_color="black",icon_size=16),
				ft.IconButton('Search',icon_color="black",icon_size=16),
				ft.Container(width=8)
				]),
			])

		return curso if EsCurso else tema

	def WdCurso(self, titulo, dt):
		wd = ft.Container(width=100, on_click=self.VerContenidoCurso, data=dt,
			border_radius=8,bgcolor=ft.colors.with_opacity(0.5, '#000000'), content=ft.Column(controls=[
			ft.Container(height=100, width=100, content=ft.Image(src="assets/imgs/presplash.png")),
			ft.Container(expand=True, padding=ft.padding.only(left=4, right=4), content=ft.Text(
				f'{titulo}',color='white',size=12)),
			]))
		return wd

	def WdTema(self, titulo, dt):
		wd = ft.Container(width=100, on_click=self.VerContenidoTema, data=dt,
			border_radius=8,bgcolor=ft.colors.with_opacity(0.5, '#000000'), content=ft.Column(controls=[
			ft.Container(height=100, width=100, content=ft.Image(src="assets/imgs/presplash.png")),
			ft.Container(expand=True, padding=ft.padding.only(left=4, right=4), content=ft.Text(
				f'{titulo}',color='white', size=12)),
			]))
		return wd

	def ListarCursos(self):
		ls = self.ObtenerCursos()
		for ke, va in ls.items():
			self.gridCursos.controls.append(self.WdCurso(va['nombre'], [ke, va]))

	def ListarTemas(self):
		ls = self.ObtenerTemas()
		for ke, va in ls.items():
			number = random.randint(1, 10)
			if number<4:
				self.gridTemas.controls.append(self.WdTema(va['nombre'], [ke, va]))
			elif number<7:
				self.gridCoins.controls.append(self.WdTema(va['nombre'], [ke, va]))
			elif number<10:
				self.gridDesaf.controls.append(self.WdTema(va['nombre'], [ke, va]))


	def ScreenInicio(self):
		theme_cls = self.page.session.get('estado')['color']
		self.ListarCursos()
		self.ListarTemas()
		#print(self.page.window_height)
		self.mainn = ft.Column(height=self.page.window_height-20)
		#Crea un Container
		TopBar = ft.Container(height=64 ,padding=8, bgcolor=f'{theme_cls}700', content=
			ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
				ft.IconButton(icon=ft.icons.LIST_ROUNDED,icon_color="black",icon_size=30),
				ft.Text('Aprendix', weight='bold', size=20),
				ft.IconButton('school',icon_color="black",icon_size=30),
				]))

		# Crea un Column
		column = ft.Column(scroll=ft.ScrollMode.HIDDEN, expand = True, controls=[
			self.ToggleButtons(),
			self.SupColecCursos('Colección de cursos', True),
			ft.Container(height=156, padding=4, content=self.gridCursos),
			self.SupColecCursos('Colección de temas', False),
			ft.Container(height=172, padding=4, content=self.gridTemas),
			ft.Container(bgcolor=f'{theme_cls}500', content=ft.Column(controls=[
				self.SupColecCursos('Consigue coins', False),
				ft.Container(height=172, padding=4, content=self.gridCoins),
				])),
			self.SupColecCursos('Desafíos\n(Exámenes semanales)', False),
			ft.Container(height=172, padding=4, content=self.gridDesaf),
			#Conociendo tu aplicación
			ft.Container(on_click=lambda e: print("test"),content=ft.Row(alignment='center',
				controls=[
				ft.Icon(name="school", size=14),
				ft.Text('Conociendo tu aplicación',size=14, weight='bold')]))
			])

		# Crea un Row de altura 64
		BottomBar = ft.Container(height=64, padding=8, bgcolor=f'{theme_cls}700', content=
			ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
				ft.IconButton(icon=ft.icons.HOME_OUTLINED,icon_color="black",icon_size=30,),
				ft.IconButton(icon='Search',icon_color="black",icon_size=30,),
				ft.IconButton(icon=ft.icons.BLUR_ON_SHARP,icon_color="black",icon_size=30,),
				ft.IconButton(icon=ft.icons.READ_MORE,icon_color="black",icon_size=30,),
				ft.IconButton(icon=ft.icons.CLOUD_DOWNLOAD_OUTLINED,icon_color="black",on_click= lambda _: self.page.go('/descargas'),icon_size=40,),
				]))

		self.mainn.controls.append(TopBar)
		self.mainn.controls.append(column)
		self.mainn.controls.append(BottomBar)
		
		return self.mainn

	def Body(self):
		return self.ScreenInicio()

	def ImprimirDatos(self):
		print(self.page.client_storage.get("colort"))

##################SECCION DE FUCIONES######################
	def VarNeed(self):
		#self.frbase = pyrebase.initialize_app(fuego)
		self.estado = self.page.session.get('estado')

	def ObtenerCursos(self):
		usuario = self.estado['usuario']
		nivel = self.estado['nivel']
		ruta = f'base/dataset/cursos/es-spa/{nivel}/cursos.json'
		return JsonLectura(ruta)

	def ObtenerTemas(self):
		usuario = self.estado['usuario']
		nivel = self.estado['nivel']
		ruta = f'base/dataset/temas/es-spa/{nivel}/temas.json'
		return JsonLectura(ruta)

	def VerContenidoCurso(self, e):
		dt = e.control.data
		self.page.client_storage.set('current_cursoid', dt[0])
		self.page.client_storage.set('current_cursodt', dt[1])
		self.page.client_storage.set('ventana', '/ialfa')
		self.page.go('/ralfa')

	def VerContenidoTema(self, e):
		dt = e.control.data
		self.page.client_storage.set('current_temaid', dt[0])
		self.page.client_storage.set('current_temadt', dt[1])
		self.page.client_storage.set('ventana', '/ialfa')
		self.page.go('/rbeta')