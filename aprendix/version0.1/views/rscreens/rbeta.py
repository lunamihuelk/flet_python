import flet as ft
from controles.jsoncontrol import JsonLectura, JsonGuardar
import random
import re
class RBeta(ft.UserControl):
	"""docstring for Home"""
	boxPregunta=ft.Column(controls=[])
	boxAlternativa=ft.Column(controls=[])
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
		dt =self.page.client_storage.get('current_temadt')
		self.ListaDePreguntas()
		self.SeleccionarPregunta()
		self.DecidirRenderizadorPregunta()
		self.RenderAlternativas()
		wd = ft.Column(height=self.page.window_height-136, width=self.page.window_width, scroll=ft.ScrollMode.HIDDEN, controls=[])
		wd1 = ft.Container(height=70, bgcolor=ft.colors.with_opacity(0.3, '#000000'), padding=ft.padding.only(left=4, right=4), content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,controls=[
			ft.Container(expand=True, content=ft.Column(controls=[
				ft.Container(expand=True, content=ft.Column(alignment='center', controls=[
					ft.Text(f'{dt["nombre"]}', size=16, weight='bold')])),
				ft.Row(height=20, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
					ft.Text('Ejercicios'),
					ft.Text('Puntos: 0|20/20|0')])])),
			ft.IconButton(icon=ft.icons.SCHOOL_OUTLINED, icon_size=40)]))
		wd2 = ft.Container(padding=ft.padding.only(left=4, right=4), content=ft.Text('La pregunta',size=16, weight='bold'))
		#wd2 = ft.Row(alignment='center', controls=[ft.Text(f'{dt["nombre"]}',size=18, weight='bold')])
		wd3 = ft.Container(padding=4, width=self.page.window_width, border_radius=ft.border_radius.only(top_left=8, bottom_right=8),
			bgcolor=ft.colors.with_opacity(0.5, '#000000'),content=self.boxPregunta)
		#wd.controls.append(wd1)
		wd4 = ft.Container(padding=ft.padding.only(left=4, right=4), content=ft.Text('Elija una alternativa',size=16, weight='bold'))
		wd5 = ft.Container(padding=4,content=self.boxAlternativa)
		#wd.controls.append(ft.Divider(height=10, color='transparent'))
		wd.controls.append(wd1)
		wd.controls.append(wd2)
		wd.controls.append(wd3)
		wd.controls.append(wd4)
		wd.controls.append(wd5)
		wd.controls.append(ft.Container(height=30))
		return wd

	def BannerSup(self):
		theme_cls= self.page.session.get('estado')['color']
		return ft.AppBar(
			leading=ft.IconButton(ft.icons.ARROW_BACK,on_click=lambda _:self.page.go('/ialfa')),
			bgcolor=f'{theme_cls}700',actions=[
			ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _:self.page.go('/'))
			])

	def Body(self):
		return self.Cuerpo()

	def BannerInf(self):
		theme_cls= self.page.session.get('estado')['color']
		return ft.BottomAppBar(bgcolor=f'{theme_cls}700', shape=ft.NotchShape.CIRCULAR,
			content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
				controls=[
				ft.IconButton(icon=ft.icons.ARROW_BACK, on_click= lambda _: self.page.go(self.ventana), icon_color=ft.colors.WHITE),
				ft.IconButton(icon=ft.icons.HOME_OUTLINED, disabled=True,icon_color=ft.colors.WHITE),
				ft.IconButton(icon=ft.icons.AUTO_AWESOME_OUTLINED, icon_color=ft.colors.WHITE),
				ft.IconButton(icon=ft.icons.REMOVE_RED_EYE_OUTLINED, on_click= lambda _: self.MostrarClave(), icon_color=ft.colors.WHITE),
				ft.IconButton(icon=ft.icons.ARROW_FORWARD, icon_color=ft.colors.WHITE),
				]
				),)

##############SECCION DE FUNCIONES##################################
	def VarNeed(self):
		self.estado = self.page.session.get('estado')
		ruta= f'base/dataset/ejercicios/es-spa/{self.estado["nivel"]}/ejercicios.json'
		self.page.client_storage.set('set_ejercicios', JsonLectura(ruta))
		self.ventana = self.page.client_storage.get('ventana')

	def ListaDePreguntas(self):
		dt =self.page.client_storage.get('current_temadt')
		self.preguntas = dt['ejercicios']
		self.listanumbers = [i for i in range(0, len(self.preguntas))]
		self.preguntaspasadas = []
		self.win, self.loss, self.cantidadpreguntas = 0, 0, len(self.listanumbers)

	def SeleccionarPregunta(self):
		self.sacar = self.listanumbers.pop(0)
		self.preguntaspasadas.append(self.sacar)
		seleccionado = self.preguntas[self.sacar]
		ejercicio = self.page.client_storage.get('set_ejercicios')[seleccionado]
		self.page.client_storage.set('current_ejercicioid', seleccionado)
		self.page.client_storage.set('current_ejerciciodt', ejercicio)

	def DecidirRenderizadorPregunta(self):
		pr = self.page.client_storage.get('current_ejerciciodt')
		pr = pr['pregunta']
		if '[/]' in pr:
			self.RenderPregunta1(pr)
		else:
			self.RenderPregunta2(pr)
	def RenderPregunta1(self):
		pr = self.page.client_storage.get('current_ejerciciodt')
		pr = pr['pregunta']
		textos = pr.split('[/]')
		for txt in textos:
			if "img:" in txt:
				t = txt[4:]
				self.boxPregunta.controls.append(ft.Text(f'{t}'))
			elif "pronu:" in txt:
				txt = f"Pronunciación: {txt[6:]}"
				self.boxPregunta.controls.append(ft.Text(f'{txt}'))
			elif "link:" in txt:
				t = txt[5:]
				self.boxPregunta.controls.append(ft.Text(f'{t}'))
			else:
				if txt != "":
					self.boxPregunta.controls.append(ft.Text('hola mundo'))

	def RenderPregunta2(self, ct):
		self.boxPregunta.controls=[]
		wd = ft.Text(disabled=False, size=16, color='blue',spans=[])
		if 'https:' in ct:
			try:
				pr = self.LimpiarTexto(ct)
			except:
				pr=['hola1', 'hola2']
				print('error')
			for word in pr:
				if 'https:' in word:
					wd.spans.append(ft.TextSpan('enlace', url=f'{word}'))
					self.boxPregunta.controls.append(wd)
				else:
					self.boxPregunta.controls.append(ft.Text(f'{word}', size=16, color='white'))

		else:
			self.boxPregunta.controls.append(ft.Text(f'{ct}', size=16, color='white'))

	def RenderAlternativas(self):
		self.boxAlternativa.controls=[]
		al = self.page.client_storage.get('current_ejerciciodt')
		al = al['alternativas']
		for a in al:
			wd=ft.Container(padding=4,width=self.page.window_width, data=a, on_click=self.VerificarRespuesta,
				border_radius=4,bgcolor=ft.colors.with_opacity(0.5, '#000000'), content=
				ft.Text(f'{a}', size=18, color='white'))
			self.boxAlternativa.controls.append(wd)

	def VerificarRespuesta(self, e):
		dt = self.page.client_storage.get('current_ejerciciodt')
		if dt['clave'] == e.control.data:
			print(self.page.client_storage.get('current_ejercicioid'))
		else:
			print('no imprime la clave')
		
	def MostrarClave(self):
		dl = self.page.client_storage.get('current_ejerciciodt')
		al = dl['alternativas']
		random.shuffle(al)
		cl = dl['clave']
		self.boxAlternativa.controls=[]
		for a in al:
			if a==cl:
				wd=ft.Container(padding=4,width=self.page.window_width, data=a, on_click=self.VerificarRespuesta,
					border_radius=4,bgcolor=ft.colors.with_opacity(0.5, '#000000'), content=
					ft.Text(f'{a}', size=18, color='cyan'))
			else:
				wd=ft.Container(padding=4,width=self.page.window_width, data=a, on_click=self.VerificarRespuesta,
					border_radius=4,bgcolor=ft.colors.with_opacity(0.5, '#000000'), content=
					ft.Text(f'{a}', size=18, color='white'))
			self.boxAlternativa.controls.append(wd)
			self.page.update()

	def LimpiarTexto(self, texto):
		lstexto=texto.split(' ')
		lsstext = []
		listafinal=[]
		esword=True
		for word in lstexto:
		    if 'https:' in word:
		        esword=False
		        stringUnido=' '.join(lsstext)
		        listafinal.append(stringUnido)
		        listafinal.append(word)
		        lsstext=[]
		    else:
		        if esword:
		            lsstext.append(word)
		        else:
		            stringUnido=' '.join(lsstext)
		            listafinal.append(stringUnido)
		            esword=True
		            lsstext=[word]
		listafinal = list(filter(bool, listafinal))
		return listafinal
"""
wd = ft.Text(
            disabled=False,
            spans=[
                ft.TextSpan("AwesomeApp 1.0 "),
                ft.TextSpan(
                    "Visit our website",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://google.com",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link,)])
"""


