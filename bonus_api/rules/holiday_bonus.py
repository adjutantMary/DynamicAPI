from ..core.base import BaseBonusRule
from decimal import Decimal
from datetime import datetime
from dateutil import tz
from dateutil.relativedelta import relativedelta


class WeekendRule(BaseBonusRule):
    code = "holiday_bonus"
    def apply(self, ctx):
        if ctx.timestamp.weekday() >= 5:
            ctx.current_bonus *= 2