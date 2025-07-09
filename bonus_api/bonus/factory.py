from bonus.models import BonusRule
from bonus_api.core.base import BaseBonusRule
from bonus_api.rules.base_rate import BaseRateRule
from bonus_api.rules.holiday_bonus import WeekendRule
from bonus_api.rules.vip_boost import VIPRule



class RuleFactory:
    @staticmethod
    def create(rule_model: BonusRule) -> BaseBonusRule:
        condition = rule_model.condition_type
        operation = rule_model.operation_type
        op_val = rule_model.operation_value or {}

        if condition == "always" and operation == "base":
            return BaseRateRule(**op_val)

        if condition == "is_weekend_or_holiday" and operation == "multiply":
            return WeekendRule(**op_val)

        if condition == "customer_status" and operation == "percent_add":
            return VIPRule(**op_val)

        raise NotImplementedError(f"No rule mapped for {condition} + {operation}")
