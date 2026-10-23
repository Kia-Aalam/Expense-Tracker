from django.db.models import Sum, Q
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import TransactionModel
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = TransactionModel.objects.filter(
            user=self.request.user
        ).select_related("category")

        type_ = self.request.query_params.get("type")
        category = self.request.query_params.get("category")
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        if type_:
            queryset = queryset.filter(type=type_)

        if category:
            queryset = queryset.filter(category_id=category)

        if start_date:
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def summary(self, request):
        totals = self.get_queryset().aggregate(
            deposits=Sum(
                "amount",
                filter=Q(type="deposit")
            ),
            withdrawals=Sum(
                "amount",
                filter=Q(type="withdrawal")
            ),
        )

        deposits = totals["deposits"] or 0
        withdrawals = totals["withdrawals"] or 0

        return Response({
            "total_deposits": deposits,
            "total_withdrawals": withdrawals,
            "balance": deposits - withdrawals,
        })


# Without a template
'''from django.db.models import Sum, Q
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
        })'''