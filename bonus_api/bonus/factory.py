from bonus.models import BonusRule
from core.base import BaseBonusRule
from rules.conditions import (
    AlwaysCondition,
    WeekendOrHolidayCondition,
    CustomerStatusCondition,
)
from rules.operations import (
    BaseBonusOperation,
    MultiplyOperation,
    PercentAddOperation,
)
from rules.dynamic import DynamicRule


CONDITION_CLASSES = {
    "always": AlwaysCondition,
    "is_weekend_or_holiday": WeekendOrHolidayCondition,
    "customer_status": CustomerStatusCondition,
}

OPERATION_CLASSES = {
    "base": BaseBonusOperation,
    "multiply": MultiplyOperation,
    "percent_add": PercentAddOperation,
}


class RuleFactory:
    
    """
    Имеет один статический метод: create
    
    Метод create:
    Создаёт новое правило бонуса на основе заданной модели rule_model
    Возвращает экземпляр DynamicRule с заданным кодом, условием и операцией
    Вызывает ошибку, если тип условия или операции не поддерживается
    """
    
    @staticmethod
    def create(rule_model) -> BaseBonusRule:
        condition_type = rule_model.condition_type
        operation_type = rule_model.operation_type

        cond_class = CONDITION_CLASSES.get(condition_type)
        op_class = OPERATION_CLASSES.get(operation_type)

        if not cond_class or not op_class:
            raise NotImplementedError(
                f"Unsupported rule type: {condition_type} + {operation_type}"
            )

        condition = cond_class(rule_model.condition_value or {})
        operation = op_class(rule_model.operation_value or {})

        return DynamicRule(
            code=rule_model.code,
            condition=condition,
            operation=operation,
        )
