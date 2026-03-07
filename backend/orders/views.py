from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):

    data = request.data.copy()
    data['user'] = request.user.id

    serializer = OrderSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Order saved successfully"})

    return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):

    orders = Order.objects.filter(user=request.user).order_by('-id')

    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)