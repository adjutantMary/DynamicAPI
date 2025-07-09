from decimal import Decimal

from bonus_api.core.registry import BonusRuleRegistry
from bonus_api.core.context import BonusCalculationContext
from bonus_api.rules.base_rate import BaseRateRule
from bonus_api.rules.vip_boost import VIPRule
from bonus_api.rules.holiday_bonus import WeekendRule

def calculate_bonus(amount, timestamp, status):
    """
    Рассчитывает общую сумму бонуса и применяет соответствующие правила начисления бонусов на основе указанной
    суммы транзакции, временной метки и статуса клиента

    Args:
        amount (Decimal): cумма транзакции, на которую должен быть рассчитан бонус
        timestamp (datetime): временная метка транзакции.
        status (str): статус клиента

    Returns:
        tuple: кортеж, содержащий общую сумму рассчитанного бонуса и список
                словарей, указывающих, какие правила были применены, и соответствующие
                суммы бонусов
    """

    ctx = BonusCalculationContext(amount, timestamp, status)
    registry = BonusRuleRegistry([BaseRateRule(), WeekendRule(), VIPRule()])
    applied = registry.apply_all(ctx)
    return ctx.current_bonus, applied