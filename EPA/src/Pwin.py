import math
from typing import Final

P_WIN_DIVIDER: Final = 400

def PWinCalculator(ELOone: int, ELOtwo: int):
    d = ELOone - ELOtwo
    return 1 / (1 + math.pow(10, d / P_WIN_DIVIDER))

def UpdateRating(CurrentRating: int, RedRating: int, BlueRating: int):
    PredictedScoreMargin = 0.004 * (RedRating - BlueRating)
    return

print(Pwin_calc(1000, 1500))
