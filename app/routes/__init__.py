from flask import Blueprint

routes = Blueprint('routes', __name__)

from .firewall import *
from .youtube import *
from .home import *


