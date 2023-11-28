from rest_framework import viewsets
from .models import Order , OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class OrdersByStatusKDS(APIView):
    def get(self, request, status_kds):
        # Use the status_kds parameter to filter orders
        orders = Order.objects.filter(status_kds=status_kds)
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": orders.values()}, status=status.HTTP_200_OK)