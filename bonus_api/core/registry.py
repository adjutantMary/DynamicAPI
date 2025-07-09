from .context import BonusCalculationContext
from .base import BaseBonusRule



class BonusRuleRegistry:
    def __init__(self, rules: list[BaseBonusRule]):
        self.rules = rules

    def apply_all(self, ctx: BonusCalculationContext) -> list[dict]:
        """
        Каждое правило применяется последовательно, изменяя текущий бонус в контексте.
        Метод отслеживает изменение бонуса для каждого правила и включает его в результат,
        если изменение бонуса положительное
        
        Args:
            ctx (BonusCalculationContext): контекст, содержащий текущее состояние расчета бонуса

        Return:
            list[dict]: список словарей, где каждый словарь содержит код "правила" и
                        сумму "бонуса", добавляемую в соответствии с этим правилом
        """

        applied = []
        for rule in self.rules:
            before = ctx.current_bonus
            rule.apply(ctx)
            delta = ctx.current_bonus - before
            if delta > 0:
                applied.append({"rule": rule.code, "bonus": delta})
        return applied
