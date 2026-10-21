from django.conf import settings
from django.db import models

class Category(models.Model):
    class Type(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"

    class Icon(models.TextChoices):
        FOOD = "🍔", "غذا و رستوران"
        GROCERY = "🛒", "خرید روزمره"
        TRANSPORT = "🚗", "حمل‌ونقل"
        FUEL = "⛽", "بنزین"
        HOME = "🏠", "خانه و اجاره"
        BILLS = "💡", "قبوض"
        HEALTH = "💊", "سلامت و دارو"
        EDUCATION = "📚", "آموزش"
        ENTERTAINMENT = "🎬", "سرگرمی"
        SHOPPING = "🛍️", "پوشاک و خرید"
        TRAVEL = "✈️", "سفر"
        GIFT = "🎁", "هدیه"
        SALARY = "💰", "حقوق و درآمد"
        INTERNET = "📱", "اینترنت و موبایل"
        OTHER = "📦", "سایر"

    class Color(models.TextChoices):
        RED = "#EF4444", "قرمز"
        ORANGE = "#F97316", "نارنجی"
        YELLOW = "#EAB308", "زرد"
        GREEN = "#22C55E", "سبز"
        TEAL = "#14B8A6", "سبزآبی"
        BLUE = "#3B82F6", "آبی"
        INDIGO = "#6366F1", "نیلی"
        PURPLE = "#A855F7", "بنفش"
        PINK = "#EC4899", "صورتی"
        GRAY = "#6B7280", "خاکستری"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="categories",
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=Type.choices)
    icon = models.CharField(
        max_length=30,
        choices=Icon.choices,
        default=Icon.OTHER,
        blank=True,
    )
    color = models.CharField(
        max_length=7,
        choices=Color.choices,
        default=Color.GRAY,
        blank=True,
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name", "type"],
                name="unique_user_category",
            )
        ]

    def __str__(self):
        return f"{self.icon} {self.name}"