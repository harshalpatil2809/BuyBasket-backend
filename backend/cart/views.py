from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from rest_framework.permissions import IsAuthenticated


class AddCart(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        product_name = request.data.get("product_name")
        price = request.data.get("price")
        quantity = request.data.get("quantity", 1)
        image = request.data.get("image")

        cart = Cart.objects.create(
            user=user,
            product_name=product_name,
            price=price,
            image=image,
            quantity=quantity
        )

        return Response({
            "message": "Product added to cart",
            "cart_id": cart.id
        }, status=status.HTTP_201_CREATED)


from rest_framework.permissions import IsAuthenticated

class ViewCart(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)

        data = []
        for item in cart_items:
            data.append({
                "id": item.id,
                "product_name": item.product_name,
                "price": item.price,
                "quantity": item.quantity,
                "image": item.image,
                "total": item.total_price()
            })

        return Response(data)