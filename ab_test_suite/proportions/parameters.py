def set_proportion_estimate_parameters(session: dict) -> (float, float, float):
    if 'confidence' in session:
        confidence = session['confidence']
    else:
        confidence = 0.95

    if 'expected_proportion' in session:
        expected_proportion = session['expected_proportion']
    else:
        expected_proportion = 0.5

    if 'expected_absolute_delta' in session:
        expected_absolute_delta = session['expected_absolute_delta']
    else:
        expected_absolute_delta = 0.1

    return confidence, expected_proportion, expected_absolute_delta
