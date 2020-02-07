from scipy.stats import norm


def get_minimum_number_result(confidence: float, expected_proportion: float,
                              expected_absolute_delta: float):
    n = int(get_minimum_number_estimate(confidence, expected_proportion, expected_absolute_delta)) + 1

    return f'Estimated minimum number of trails per group: {n}'


def get_minimum_number_estimate(confidence: float, expected_proportion: float,
                                expected_absolute_delta: float):
    z_confidence = norm.ppf((1 + confidence) / 2)
    p_hat = expected_proportion + expected_absolute_delta / 2

    return 2 * (z_confidence ** 2) * p_hat * (1 - p_hat) / (expected_absolute_delta ** 2)
