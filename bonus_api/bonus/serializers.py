from rest_framework import serializers


class BonusCalculationInputSerializer(serializers.Serializer):
    transaction_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    timestamp = serializers.DateTimeField()
    customer_status = serializers.ChoiceField(choices=["regular", "vip"])

class AppliedRuleSerializer(serializers.Serializer):
    rule = serializers.CharField()
    bonus = serializers.DecimalField(max_digits=10, decimal_places=2)

class BonusCalculationResultSerializer(serializers.Serializer):
    total_bonus = serializers.DecimalField(max_digits=10, decimal_places=2)
    applied_rules = AppliedRuleSerializer(many=True)


