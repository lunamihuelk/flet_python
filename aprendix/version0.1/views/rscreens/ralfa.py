import flet as ft
from controles.jsoncontrol import JsonLectura, JsonGuardar

class RAlfa(ft.UserControl):
	gridUnidades= ft.Row(scroll=ft.ScrollMode.HIDDEN)
	"""docstring for Home"""
	def __init__(self, page):
		super().__init__()
		self.page = page
		self.VarNeed()

	def WdUnidad(self, titulo, dt):
		wd = ft.Container(width=100, on_click=self.VerContenidoCurso, data=dt,
			border_radius=8,bgcolor=ft.colors.with_opacity(0.5, '#000000'), content=ft.Column(controls=[
			ft.Container(height=100, width=100, content=ft.Image(src="assets/imgs/presplash.png")),
			ft.Container(expand=True, padding=ft.padding.only(left=4, right=4), content=ft.Text(
				f'{titulo}',color='white',size=12)),
			]))
		return wd

	def ListarUnidades(self):
		ls = [f'hola 000{i}' for i in range(10)]
		#for ke, va in ls.items():
		for ke in ls:
			self.gridTemas.controls.append(self.WdUnidad(va['nombre'], [ke, va]))

	def Cuerpo(self):
		dt =self.page.client_storage.get('current_cursodt')
		wd = ft.Column(height=self.page.window_height-56, width=self.page.window_width, scroll=ft.ScrollMode.HIDDEN, controls=[])
		wd2 = ft.Row(alignment='center', controls=[ft.Text(f'{dt["nombre"]}',size=18, weight='bold')])
		wd3 = ft.Row(alignment='center', controls=[ft.Text(f'{dt["nivel"]}',size=16, weight='bold')])
		#wd.controls.append(wd1)
		wd4 = ft.Container(padding=ft.padding.only(left=4, right=4), content=ft.Text('Contenido',size=16, weight='bold'))
		wd5 = ft.Column()
		contenido = ft.Text(f'{dt["descripcion"]}')
		wd5.controls.append(contenido)
		wd.controls.append(wd2)
		wd.controls.append(wd3)
		wd.controls.append(ft.Container(height=156, padding=4, content=self.gridUnidades))
		wd.controls.append(wd4)
		wd.controls.append(wd5)
		wd.controls.append(ft.Container(height=30))
		return wd

	def BannerSup(self):
		theme_cls= self.page.session.get('estado')['color']
		return ft.AppBar(
			leading=ft.IconButton(ft.icons.ARROW_BACK,on_click=lambda _:self.page.go('/ialfa')),
			bgcolor=f'{theme_cls}700',actions=[
			ft.IconButton(icon='data_saver_on', on_click=lambda _:self.page.go('/malfa'),),
			ft.IconButton(icon='more_vert', on_click=lambda _:self.page.go('/ialfa'),)
			])

	def Body(self):
		return self.Cuerpo()

##############SECCION DE FUNCIONES##################################
	def VarNeed(self):
		self.estado = self.page.session.get('estado')