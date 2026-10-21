from rest_framework import serializers
from .models import CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        read_only_fields = ["id"]

    def validate(self, attrs):
        user = self.context["request"].user
        name = attrs.get("name", getattr(self.instance, "name", None))
        type_ = attrs.get("type", getattr(self.instance, "type", None))

        qs = CategoryModel.objects.filter(user=user, name=name, type=type_)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("این دسته‌بندی قبلاً ساخته شده.")
        return attrs