from rest_framework import viewsets
from .models import Order , OrderSerializer , Table , TableSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
class OrdersByStatusKDS(APIView):
    def get(self, request, status_kds):
        orders = Order.objects.filter(status_kds=status_kds)
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": orders.values()}, status=status.HTTP_200_OK)