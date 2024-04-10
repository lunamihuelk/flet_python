from views.cero import Cero
from views.iscreens.ialfa import IAlfa

from views.mscreens.malfa import MAlfa

from views.rscreens.ralfa import RAlfa
from views.rscreens.rbeta import RBeta

from views.home import Home
from views.login import Login

from views.descargas import Descargas

lsViews = {
'/': Cero,
'/ialfa': IAlfa,
'/home': Home,
'/login': Login,

'/malfa': MAlfa,

'/ralfa': RAlfa,
'/rbeta': RBeta,

'/descargas': Descargas,
}