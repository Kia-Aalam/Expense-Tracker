from django.db.models import Q
from rest_framework import viewsets, permissions

from .models import CategoryModel
from .serializers import CategorySerializer
from .permissions import IsOwnerOrReadOnlySystem

class CategoryViewSet(viewsets.ModelViewSet):
    #queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnlySystem]
    
    def get_queryset(self):
        qs = CategoryModel.objects.filter(
            Q(user=self.request.user) | Q(user__isnull=True)
        )
        type_ = self.request.query_params.get("type")
        if type_:
            qs = qs.filter(type=type_)
        return qs.order_by("name")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)