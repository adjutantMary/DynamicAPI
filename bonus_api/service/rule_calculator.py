from decimal import Decimal
from datetime import datetime
from bonus.factory import RuleFactory
from core.registry import BonusRuleRegistry
from core.context import BonusCalculationContext
from bonus.repository import BonusRuleRepository
from typing import Tuple, List, Dict


def calculate_bonus(
    amount: Decimal,
    timestamp: datetime,
    status: str,
) -> Tuple[Decimal, List[Dict[str, Decimal]]]:
    """
    Расчет общей суммы бонуса и список применяемых правил

    Args:
        amount (Decimal): сумма транзакции, на которую должен быть рассчитан бонус
        timestamp (datetime): дата и время совершения транзакции
        status (str): статус клиента, например, "обычный" или "vip"

    Returns:
        Tuple[Decimal, List[Dict[str, Decimal]]]: кортеж, содержащий общую сумму бонуса в десятичной
        системе счисления и список словарей, где каждый словарь содержит код правила и сумму бонуса,
        применяемую в соответствии с этим правилом
    """

    ctx = BonusCalculationContext(amount, timestamp, status)

    repo = BonusRuleRepository()
    rule_models = repo.get_active_rules()
    rules = [RuleFactory.create(r) for r in rule_models]

    registry = BonusRuleRegistry(rules)
    applied = registry.apply_all(ctx)

    return ctx.current_bonus, applied
