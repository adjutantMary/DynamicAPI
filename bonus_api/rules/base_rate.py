from ..core.base import BaseBonusRule
from decimal import Decimal


class BaseRateRule(BaseBonusRule):
    code = "base_rate"
    def apply(self, ctx):
        bonus = ctx.amount // Decimal(10)
        ctx.current_bonus += bonus
