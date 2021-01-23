from ab_test_suite.proportions.parameters import set_proportion_estimate_parameters, set_significance_parameters
from ab_test_suite.proportions.significance import get_results
from ab_test_suite.proportions.size_estimate import get_minimum_number_result
from flask import Blueprint
from flask import render_template, session, request, redirect, url_for

routes_proportions = Blueprint('routes_proportions', __name__)


@routes_proportions.route("/proportions")
def proportions():
    confidence_estimate, expected_proportion, expected_absolute_delta = set_proportion_estimate_parameters(session)
    minimum_number_result = get_minimum_number_result(confidence_estimate, expected_proportion, expected_absolute_delta)

    confidence_significance, nA, sA, nB, sB = set_significance_parameters(session)

    descriptive_result, test_result = get_results(confidence_significance, nA, sA, nB, sB)

    return render_template('proportions.html',
                           confidence_estimate=confidence_estimate,
                           expected_proportion=expected_proportion,
                           expected_absolute_delta=expected_absolute_delta,
                           minimum_number_result=minimum_number_result,
                           confidence_significance=confidence_significance,
                           nA=nA,
                           sA=sA,
                           nB=nB,
                           sB=sB,
                           descriptive_result=descriptive_result,
                           test_result=test_result)


@routes_proportions.route("/proportions/set_estimate_params", methods=['POST'])
def set_estimate_params():
    for id in ['confidence_estimate', 'expected_proportion', 'expected_absolute_delta']:
        session[id] = float(request.form[id])
    return redirect(url_for(".proportions"))


@routes_proportions.route("/proportions/set_significance_params", methods=['POST'])
def set_significance_params():
    session['confidence_significance'] = float(request.form['confidence_significance'])

    for id in ['nA', 'sA', 'nB', 'sB']:
        session[id] = int(request.form[id])

    return redirect(url_for(".proportions"))
