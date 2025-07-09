from bonus.models import BonusRule


class BonusRuleRepository:
    """Слой для работы с ORM"""

    def get_active_rules(self):
        return BonusRule.objects.filter(is_active=True).order_by("priority")

    # Дополнительный метод для расширения логики
    def get_all_rules(self):
        return BonusRule.objects.all().order_by("priority")
