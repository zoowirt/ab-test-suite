from collections import namedtuple

import numpy as np
from scipy.stats import norm
from typing import Optional

ProportionResult = namedtuple('proportion_result', ['model_name', 'n', 's'])


class zTest:

    def __init__(self, confidence: float):
        self.confidence = confidence

    def decide(self, A: ProportionResult, B: ProportionResult) -> Optional[str]:

        Z = self._get_Z_value(A, B)
        if norm.cdf(np.abs(Z)) >= (1 + self.confidence) / 2:
            if Z > 0:
                return A.model_name
            else:
                return B.model_name
        else:
            return None

    def get_confidence_level(self, A: ProportionResult, B: ProportionResult) -> float:
        Z = self._get_Z_value(A, B)
        return 2 * norm.cdf(np.abs(Z)) - 1

    def get_leader(self, A: ProportionResult, B: ProportionResult) -> str:
        pA = A.s / A.n
        pB = B.s / B.n

        return A.model_name if pA >= pB else B.model_name

    def get_looser(self, A: ProportionResult, B: ProportionResult) -> str:
        pA = A.s / A.n
        pB = B.s / B.n

        return A.model_name if pA < pB else B.model_name

    def _get_Z_value(self, A: ProportionResult, B: ProportionResult) -> float:
        Z_nominator = A.s / A.n - B.s / B.n
        p_hat = (A.s + B.s) / (A.n + B.n)
        Z_denominator = np.sqrt(p_hat * (1 - p_hat) * (1 / A.n + 1 / B.n))

        if Z_denominator != 0:
            return Z_nominator / Z_denominator
        else:
            return 0

    def _get_mean_std(self, A: ProportionResult, B: ProportionResult) -> (float, float):
        pA = A.s/A.n
        pB = B.s/B.n

        mean = pA - pB
        std = np.sqrt(pA*(1-pA)/ A.n + pB*(1-pB)/ B.n)

        return mean, std
