from flask import Blueprint
routes = Blueprint('routes', __name__)

from .polls import *
from .login import *
from .answers import *
from .tags import *