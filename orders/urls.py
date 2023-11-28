from django.urls import path

from . import views

urlpatterns = [
    path('orders-by-status/<str:status_kds>/', views.OrdersByStatusKDS.as_view(), name='orders-by-status'),
]
