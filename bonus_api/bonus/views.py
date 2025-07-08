from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    BonusCalculationInputSerializer,
    BonusCalculationResultSerializer,
)
from .service import RuleEngine  # ты реализуешь это отдельно


class CalculateBonusView(APIView):
    def post(self, request):
        serializer = BonusCalculationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        engine = RuleEngine(
            amount=data["transaction_amount"],
            timestamp=data["timestamp"],
            customer_status=data["customer_status"],
        )

        total_bonus, applied_rules = engine.calculate()

        result = BonusCalculationResultSerializer(
            {"total_bonus": total_bonus, "applied_rules": applied_rules}
        )

        return Response(result.data, status=status.HTTP_200_OK)
