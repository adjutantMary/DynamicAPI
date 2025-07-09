from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BonusCalculationInputSerializer

from service.rule_calculator import calculate_bonus


class CalculateBonusView(APIView):
    def post(self, request):
        serializer = BonusCalculationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        total_bonus, applied_rules = calculate_bonus(
            amount=data["transaction_amount"],
            timestamp=data["timestamp"],
            status=data["customer_status"],
        )

        response = {"total_bonus": total_bonus, "applied_rules": applied_rules}

        return Response(response)
