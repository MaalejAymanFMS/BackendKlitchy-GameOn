from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet,OrdersByStatusKDS,TableViewSet
router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'tables', TableViewSet)
urlpatterns = [
    path("user/",include("user.urls")),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path("orders/",include("orders.urls")),
]