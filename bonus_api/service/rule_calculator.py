from decimal import Decimal

from bonus.factory import RuleFactory
from core.registry import BonusRuleRegistry
from core.context import BonusCalculationContext
from bonus.repository import BonusRuleRepository

def calculate_bonus(amount, timestamp, status):
    ctx = BonusCalculationContext(amount, timestamp, status)

    repo = BonusRuleRepository()
    rule_models = repo.get_active_rules()
    rules = [RuleFactory.create(r) for r in rule_models]

    registry = BonusRuleRegistry(rules)
    applied = registry.apply_all(ctx)

    return ctx.current_bonus, applied