from flask import Blueprint
from flask import render_template

routes = Blueprint('routes', __name__)


@routes.route("/")
def main():
    return render_template('main.html')

