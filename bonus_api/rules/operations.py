from decimal import Decimal


class BaseOperation:
    def apply(self, ctx):
        raise NotImplementedError


class BaseBonusOperation(BaseOperation):
    def __init__(self, config):
        self.per_amount = Decimal(config.get("per_amount", 10))

    def apply(self, ctx):
        bonus = ctx.amount // self.per_amount
        ctx.current_bonus += bonus
        return bonus


class MultiplyOperation(BaseOperation):
    def __init__(self, config):
        self.factor = Decimal(config.get("factor", 1))

    def apply(self, ctx):
        before = ctx.current_bonus
        ctx.current_bonus *= self.factor
        return ctx.current_bonus - before


class PercentAddOperation(BaseOperation):
    def __init__(self, config):
        self.percent = Decimal(config.get("value", 0)) / 100

    def apply(self, ctx):
        add = ctx.current_bonus * self.percent
        ctx.current_bonus += add
        return add
