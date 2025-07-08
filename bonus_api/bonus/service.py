from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from .models import BonusRule, RuleConditionType, RuleOperationType
import holidays


class RuleEngine:
    def __init__(self, amount, timestamp, customer_status):
        self.amount = Decimal(amount)
        self.timestamp = timestamp
        self.customer_status = customer_status
        self.applied_rules = []
        self.current_bonus = Decimal("0.00")

    def calculate(self):
        rules = BonusRule.objects.filter(is_active=True).order_by('priority')

        for rule in rules:
            if not self._check_condition(rule):
                continue

            bonus_before = self.current_bonus
            self._apply_operation(rule)
            bonus_added = self.current_bonus - bonus_before

            self.applied_rules.append({
                "rule": rule.code,
                "bonus": bonus_added.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            })

        return (
            self.current_bonus.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
            self.applied_rules
        )

    def _check_condition(self, rule: BonusRule):
        cond_type = rule.condition_type
        cond_value = rule.condition_value or {}

        if cond_type == RuleConditionType.ALWAYS:
            return True

        if cond_type == RuleConditionType.IS_WEEKEND_OR_HOLIDAY:
            is_weekend = self.timestamp.weekday() >= 5  # 5=Saturday, 6=Sunday
            is_holiday = self._is_holiday(self.timestamp.date())
            return is_weekend or is_holiday

        if cond_type == RuleConditionType.CUSTOMER_STATUS:
            return cond_value.get("status") == self.customer_status

        return False

    def _apply_operation(self, rule: BonusRule):
        op_type = rule.operation_type
        op_value = rule.operation_value

        if op_type == RuleOperationType.BASE:
            rate = Decimal(op_value.get("per_amount", 10))
            bonus = (self.amount / rate).to_integral_value(rounding=ROUND_HALF_UP)
            self.current_bonus += bonus

        elif op_type == RuleOperationType.MULTIPLY:
            factor = Decimal(op_value.get("factor", 1))
            self.current_bonus *= factor

        elif op_type == RuleOperationType.PERCENT_ADD:
            percent = Decimal(op_value.get("value", 0)) / 100
            self.current_bonus += self.current_bonus * percent

    def _is_holiday(self, date):
        ru_holidays = holidays.RU()
        return date in ru_holidays
