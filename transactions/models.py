from django.db import models
from django.conf import settings


class TransactionModel(models.Model):
    class Type(models.TextChoices):
        DEPOSIT = "deposit", "Deposit"      
        WITHDRAWAL = "withdrawal", "Withdrawal"  

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="transactions")
    category = models.ForeignKey("categories.CategoryModel", on_delete=models.PROTECT, related_name="transactions")
    type = models.CharField(max_length=10, choices=Type.choices)
    amount = models.DecimalField(max_digits=14, decimal_places=0)
    date = models.DateField()
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-id"]
        indexes = [models.Index(fields=["user", "date"])]