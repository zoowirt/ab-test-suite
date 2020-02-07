from ab_test_suite.proportions.parameters import set_proportion_estimate_parameters
from ab_test_suite.proportions.size_estimate import get_minimum_number_result
from flask import Blueprint
from flask import render_template, session, request, redirect, url_for

routes_proportions = Blueprint('routes_proportions', __name__)


@routes_proportions.route("/comparing-proportions")
def proportions():
    confidence, expected_proportion, expected_absolute_delta = set_proportion_estimate_parameters(session)
    minimum_number_result = get_minimum_number_result(confidence, expected_proportion, expected_absolute_delta)

    return render_template('proportions.html',
                           confidence=confidence,
                           expected_proportion=expected_proportion,
                           expected_absolute_delta=expected_absolute_delta,
                           minimum_number_result=minimum_number_result)


@routes_proportions.route("/comparing-proportions/set_estimate_params", methods=['POST'])
def set_estimate_params():
    session['confidence'] = float(request.form['confidence'])
    session['expected_proportion'] = float(request.form['expected_proportion'])
    session['expected_absolute_delta'] = float(request.form['expected_absolute_delta'])
    return redirect(url_for(".proportions"))
