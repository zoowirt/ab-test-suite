def set_proportion_estimate_parameters(session: dict) -> (float, float, float):
    if 'confidence_estimate' in session:
        confidence_estimate = session['confidence_estimate']
    else:
        confidence_estimate = 0.95

    if 'expected_proportion' in session:
        expected_proportion = session['expected_proportion']
    else:
        expected_proportion = 0.5

    if 'expected_absolute_delta' in session:
        expected_absolute_delta = session['expected_absolute_delta']
    else:
        expected_absolute_delta = 0.1

    return confidence_estimate, expected_proportion, expected_absolute_delta


def set_significance_parameters(session: dict) -> (float, int, int, int, int):
    if 'confidence_significance' in session:
        confidence_significance = session['confidence_significance']
    else:
        confidence_significance = 0.95

    if 'nA' in session:
        nA = session['nA']
    else:
        nA = 1000

    if 'sA' in session:
        sA = session['sA']
    else:
        sA = 500

    if 'nB' in session:
        nB = session['nB']
    else:
        nB = 1000

    if 'sB' in session:
        sB = session['sB']
    else:
        sB = 400

    return confidence_significance, nA, sA, nB, sB
