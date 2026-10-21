from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/accounts/', include('accounts.urls')),
    path('api/categories/', include('categories.urls')),
    #path('api/wallets/', include('wallets.urls')),
    #path('api/transactions/', include('transactions.urls')),
]