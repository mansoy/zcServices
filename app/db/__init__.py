from flask import Blueprint

data = Blueprint('data', __name__) #, subdomain='data')

from . import datas