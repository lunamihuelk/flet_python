from flet import *
from views.home import Home
from views.login import Login

def views_handler(page):
	return {
		'/home':View(
			route='/in',
			controls=[
				Home(page)
			]
			),
		'/login':View(
			route='/login',
			controls=[
				Login(page)
			]
			)
	}