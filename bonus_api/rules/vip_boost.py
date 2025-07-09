from ..bonus.models import BaseBonusRule
from  decimal import Decimal


class VIPRule(BaseBonusRule):
    code = "vip_boost"
    def apply(self, ctx):
        if ctx.customer_status == "vip":
            ctx.current_bonus *= Decimal('1.4')