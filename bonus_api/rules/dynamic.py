
from core.base import BaseBonusRule

class DynamicRule(BaseBonusRule):
    def __init__(self, code, condition, operation):
        self.code = code
        self.condition = condition
        self.operation = operation

    def apply(self, ctx):
        if self.condition.check(ctx):
            return self.operation.apply(ctx)