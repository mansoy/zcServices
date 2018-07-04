from flask import Blueprint

odds = Blueprint('odds', __name__)#, subdomain='odds')


from . import views
