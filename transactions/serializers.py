from rest_framework import serializers
from .models import TransactionModel


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = ["id", "user", "category", "type", "amount", "date", "note", "created_at"]
        read_only_fields = ["id", "user", "created_at"]