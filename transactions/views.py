from django.db.models import Sum, Q
from rest_framework.views import APIView
from rest_framework.response import Response


class TransactionView(APIView):
    def get(self, request):
        totals = request.user.transactions.aggregate(
            deposits=Sum("amount", filter=Q(type="deposit")),
            withdrawals=Sum("amount", filter=Q(type="withdrawal")),
        )
        deposits = totals["deposits"] or 0
        withdrawals = totals["withdrawals"] or 0
        return Response({
            "total_deposits": deposits,
            "total_withdrawals": withdrawals,
            "balance": deposits - withdrawals,
        })