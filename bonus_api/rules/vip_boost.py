from core.base import BaseBonusRule
from decimal import Decimal


class VIPRule(BaseBonusRule):
    code = "vip_boost"

    def __init__(self, value: int = 40):
        self.percent = Decimal(value) / 100

    def apply(self, ctx):
        if ctx.customer_status == "vip":
            ctx.current_bonus += ctx.current_bonus * self.percent
