from ab_test_suite.proportions.zTest import zTest, ProportionResult


def get_results(confidence_significance: float, nA: int, sA: int, nB: int, sB: int) -> (str, str):
    z_test = zTest(confidence_significance)

    pA = round(sA / nA, 3)
    pB = round(sB / nB, 3)

    if pA > 1 or pB > 1:
        descriptive_result = 'Number of successes cannot exceed number of trials. Please check your input.'
        return descriptive_result, ''

    descriptive_result = f'Descriptive result: rate group A: {pA}, rate group: {pB}'

    result_A = ProportionResult('A', nA, sA)
    result_B = ProportionResult('B', nB, sB)

    decision = z_test.decide(result_A, result_B)
    looser = z_test.get_looser(result_A, result_B)
    confidence_level = int(round(z_test.get_confidence_level(result_A, result_B) * 100))

    if confidence_level == 100:
        confidence_level = 99

    if decision:
        test_result = f'The confidence level is {confidence_level}%. The rate of {decision} is significantly larger than that of {looser}.'
    else:
        test_result = f'The confidence level of {confidence_level}% does not exceed {int(confidence_significance*100)}%. The rates of A and B do thus not differ significantly.'

    return descriptive_result, test_result
