from decimal import Decimal

from bonus_api.bonus.factory import RuleFactory
from bonus_api.bonus.models import BonusRule
from bonus_api.core.registry import BonusRuleRegistry
from bonus_api.core.context import BonusCalculationContext



def calculate_bonus(amount, timestamp, status):
    ctx = BonusCalculationContext(amount, timestamp, status)

    rule_models = BonusRule.objects.filter(is_active=True).order_by("priority")
    rules = [RuleFactory.create(r) for r in rule_models]

    registry = BonusRuleRegistry(rules)
    applied = registry.apply_all(ctx)
    return ctx.current_bonus, applied