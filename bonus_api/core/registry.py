from .context import BonusCalculationContext
from .base import BaseBonusRule
from bonus.models import BonusLog

import logging

logger = logging.getLogger(__name__)


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

        logger.info("Регистрация правил")

        for rule in self.rules:
            before = ctx.current_bonus
            rule.apply(ctx)
            delta = ctx.current_bonus - before

            logger.debug(
                f"Правило: {rule.code} | {before} → {ctx.current_bonus} | ∆ = {delta}"
            )

            if delta > 0:
                applied.append({"rule": rule.code, "bonus": delta})

            logger.info(f"Расчёт завершён. Бонус: {ctx.current_bonus}")

            BonusLog.objects.create(
                rule_code=rule.code, bonus_delta=delta, total_bonus=ctx.current_bonus
            )
        return applied
