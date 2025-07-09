from core.base import BaseBonusRule
from decimal import Decimal


class WeekendRule(BaseBonusRule):
    code = "holiday_bonus"

    def __init__(self, factor: float = 2.0):
        self.factor = Decimal(factor)

    def apply(self, ctx):
        if ctx.timestamp.weekday() >= 5:
            ctx.current_bonus *= self.factor
