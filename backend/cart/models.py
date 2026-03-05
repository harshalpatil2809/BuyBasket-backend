from django.db import models
from django.conf import settings

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carts')
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image_url = models.URLField(max_length=500)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product_name} - {self.user.email}"