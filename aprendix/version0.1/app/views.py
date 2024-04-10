from flet import *
from views.cero import Cero
from views.iscreens.ialfa import IAlfa
from views.home import Home
from views.login import Login
from flet import Page
def views_handler(page):

	return {
		'/':View(route='/', controls=[Cero(page)]),
		'/ialfa':View(route='/ialfa', bgcolor='blue200', controls=[IAlfa(page)]),
		'/home':View(route='/home',controls=[Home(page)]),
		'/login':View(
			route='/login',
			controls=[
				Login(page)
			]
			)
	}