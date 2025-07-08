from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField


class RuleConditionType(models.TextChoices):
    """Правила расчета бонуса"""
    ALWAYS = "always", _("Always applies")
    IS_WEEKEND_OR_HOLIDAY = "is_weekend_or_holiday", _("Weekend or Holiday")
    CUSTOMER_STATUS = "customer_status", _("Customer Status")


class RuleOperationType(models.TextChoices):
    """Правила расчета бонуса"""
    BASE = "base", _("Base bonus per amount")
    MULTIPLY = "multiply", _("Multiply bonus")
    PERCENT_ADD = "percent_add", _("Add percentage to bonus")


class BonusRule(models.Model):
    
    """Задаёт, что делает правило, при каких условиях и в каком порядке применяется"""
    
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    condition_type = models.CharField(
        max_length=32,
        choices=RuleConditionType.choices
    )
    condition_value = models.JSONField(blank=True, null=True)
    operation_type = models.CharField(
        max_length=32,
        choices=RuleOperationType.choices
    )
    operation_value = models.JSONField()

    priority = models.PositiveIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return f"{self.code} ({self.condition_type} → {self.operation_type})"

