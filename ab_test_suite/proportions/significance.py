from ab_test_suite.proportions.zTest import zTest, ProportionResult


def get_results(confidence_significance: float, nA: int, sA: int, nB: int, sB: int) -> (str, str):
    z_test = zTest(confidence_significance)

    pA = round(sA / nA, 3)
    pB = round(sB / nB, 3)

    if pA > 1 or pB > 1:
        descriptive_result = 'Number of successes cannot exceed number of trials. Please check your input.'
        return descriptive_result, ''

    descriptive_result = f'Descriptive result: proportion group A: {pA}, proportion group: {pB}'

    result_A = ProportionResult('A', nA, sA)
    result_B = ProportionResult('B', nB, sB)

    decision = z_test.decide(result_A, result_B)
    looser = z_test.get_looser(result_A, result_B)
    significance = int(round(z_test.get_significance(result_A, result_B) * 100))

    if significance == 100:
        significance = 99

    if decision:
        test_result = f'Group {decision} is significantly better than group {looser}. The confidence level is {significance}%'
    else:
        test_result = f'The difference between groups A and B is not significant. The confidence level is only {significance}%'

    return descriptive_result, test_result
