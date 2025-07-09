from core.base import BaseBonusRule
from decimal import Decimal


class BaseRateRule(BaseBonusRule):
    code = "base_rate"

    def __init__(self, per_amount: int = 10):
        self.per_amount = Decimal(per_amount)

    def apply(self, ctx):
        bonus = ctx.amount // self.per_amount
        ctx.current_bonus += bonus
