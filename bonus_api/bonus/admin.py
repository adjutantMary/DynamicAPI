from django.contrib import admin
from .models import BonusRule
from django import forms
from django.contrib.postgres.fields import JSONField
from django.db import models


class JSONTextAreaWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {"rows": 4, "cols": 60})
        super().__init__(*args, **kwargs)


class BonusRuleAdminForm(forms.ModelForm):
    class Meta:
        model = BonusRule
        fields = "__all__"
        widgets = {
            "condition_value": JSONTextAreaWidget(),
            "operation_value": JSONTextAreaWidget(),
        }

    def clean(self):
        cleaned_data = super().clean()
        condition_type = cleaned_data.get("condition_type")
        condition_value = cleaned_data.get("condition_value")
        operation_type = cleaned_data.get("operation_type")
        operation_value = cleaned_data.get("operation_value")
        
        if operation_type == "percent_add" and "value" not in operation_value:
            raise forms.ValidationError("Для percent_add нужно указать 'value' в operation_value")

        if condition_type == "customer_status":
            if "status" not in condition_value:
                raise forms.ValidationError("Для customer_status нужно указать {'status': 'vip'}")

        return cleaned_data
    
    
@admin.register(BonusRule)
class BonusRuleAdmin(admin.ModelAdmin):
    form = BonusRuleAdminForm
    list_display = ("code", "condition_type", "operation_type", "priority", "is_active")
    list_filter = ("is_active", "condition_type", "operation_type")
    search_fields = ("code", "description")
    ordering = ("priority",)
