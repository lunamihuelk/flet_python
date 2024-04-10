import flet as ft
from controles.jsoncontrol import JsonLectura, JsonGuardar
from base.basedict import fuego, nouser
import pyrebase

class Descargas(ft.UserControl):
	"""docstring for Home"""
	def __init__(self, page):
		super().__init__()
		self.page = page
		self.estado = self.page.session.get('estado')
		self.frbase = pyrebase.initialize_app(fuego)

	def Cuerpo(self):
		wd = ft.Column(height=self.page.window_height-56, width=self.page.window_width, scroll=ft.ScrollMode.HIDDEN, controls=[])
		wd1 = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
			ft.Text('Descargar \nDatos', size=16, weight='bold'),
			ft.FilledTonalButton(text="Descarga general")])
		wd2 = ft.Container(padding=ft.padding.only(left=4,right=4), content=ft.Column([
			ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
				ft.Text('- Nivel universitario'),
				ft.IconButton(icon='download', on_click=lambda _:self.DescargaPorNivel('univ'))
				]),
			ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
				ft.Text('- Nivel pre_universitario'),
				ft.IconButton(icon='download', on_click=lambda _:self.DescargaPorNivel('preu'))
				]),
			ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
				ft.Text('- Nivel secundario'),
				ft.IconButton(icon='download', on_click=lambda _:self.DescargaPorNivel('secu'))
				]),
			ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
				ft.Text('- Nivel primario'),
				ft.IconButton(icon='download', on_click=lambda _:self.DescargaPorNivel('prim'))
				]),
			ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
				ft.Text('Actualización del temario'),
				ft.IconButton(icon='update')
				]),
			]))
		wd3 = ft.Container(padding=ft.padding.only(left=4,right=4),content=ft.Column([
			ft.Text('Anuncio y/o novedades', size=16, weight='bold'),
			ft.Container(padding=ft.padding.only(left=2,right=2), content=
				ft.Text('Mantenimiento los dias sábados'))]))
		wd4 = ft.Container(padding=ft.padding.only(left=4,right=4),content=ft.Column([
			ft.Text('Anuncio y/o novedades', size=16, weight='bold'),
			ft.Container(padding=ft.padding.only(left=2,right=2), content=
				ft.Text('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation'))]))
		wd.controls.append(wd1)
		wd.controls.append(wd2)
		wd.controls.append(wd3)
		wd.controls.append(wd4)
		wd.controls.append(ft.Container(height=50))
		return wd

	def BannerSup(self):
		theme_cls= self.page.session.get('estado')['color']
		return ft.AppBar(title=ft.Text("Sección descargas"), 
			leading=ft.IconButton(ft.icons.ARROW_BACK,on_click=lambda _:self.page.go('/ialfa')),
			bgcolor=f'{theme_cls}700',actions=[ft.IconButton(ft.icons.ARROW_BACK,
			on_click=lambda _:self.page.go('/'))])

	def Body(self):
		return self.Cuerpo()

	def Bannerinferior(self):
		theme_cls= self.page.session.get('estado')['color']
		return ft.BottomAppBar(bgcolor=f'{theme_cls}700', shape=ft.NotchShape.CIRCULAR,
			content=ft.Row(
				controls=[
				ft.IconButton(icon=ft.icons.MENU, on_click= lambda _: self.page.go('/'), icon_color=ft.colors.WHITE),
				ft.Container(expand=True),
				ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
				ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
				]
				),)
	
	def ImprimirDatos(self):
		print(self.page.client_storage.get("colort"))

	def VerificarInternet(self):
		auth = self.frbase.auth()
		user = auth.sign_in_with_email_and_password(nouser["email"], nouser["password"])
		self.estado['token'] = user['idToken']
		JsonGuardar('base/estadoapp.json', self.estado)
		print('token obtenido')

##################Parte funciones########################
	def DescargaPorNivel(self, niv='preu'):
		usuario = self.estado['usuario']
		#self.VerificarInternet()
		self.DescargarCursos(niv)
		self.DescargarUnidades(niv)
		self.DescargarTemas(niv)
		self.DescargarEjercicios(niv)
		print('Descarga exitosa')

	def DescargarCursos(self, nivel):
		db = self.frbase.database()
		data = db.child("dataset").child("cursos").child("es-spa").child(nivel).get(self.estado['token'])
		ruta = f'base/dataset/cursos/es-spa/{nivel}/cursos.json'
		cursos = {}
		for dt in data.each():
			cursos[dt.key()] = dt.val()
		JsonGuardar(ruta, cursos)

	def DescargarUnidades(self, nivel):
		db = self.frbase.database()
		data = db.child("dataset").child("unidades").child("es-spa").child(nivel).get(self.estado['token'])
		ruta = f'base/dataset/unidades/es-spa/{nivel}/unidades.json'
		unidades = {}
		for dt in data.each():
			unidades[dt.key()] = dt.val()
		JsonGuardar(ruta, unidades)

	def DescargarTemas(self, nivel):
		db = self.frbase.database()
		data = db.child("dataset").child("temas").child("es-spa").child(nivel).get(self.estado['token'])
		ruta = f'base/dataset/temas/es-spa/{nivel}/temas.json'
		temas = {}
		for dt in data.each():
			temas[dt.key()] = dt.val()
		JsonGuardar(ruta, temas)

	def DescargarEjercicios(self, nivel):
		db = self.frbase.database()
		data = db.child("dataset").child("ejercicios").child("es-spa").child(nivel).get(self.estado['token'])
		ruta = f'base/dataset/ejercicios/es-spa/{nivel}/ejercicios.json'
		ejercicios = {}
		for dt in data.each():
			ejercicios[dt.key()] = dt.val()
		JsonGuardar(ruta, ejercicios)