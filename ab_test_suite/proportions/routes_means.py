from flask import Blueprint
from flask import render_template

routes_means = Blueprint('routes_means', __name__)


@routes_means.route("/means")
def means():
    return render_template('means.html')