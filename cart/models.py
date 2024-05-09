from django.db import models
from users.models import User
from product.models import Product 

class Cart(models.Model):
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_quantity = models.PositiveIntegerField(default=1)
    #extra field
    cart_created_date = models.DateTimeField(auto_now_add=True,editable=False)
    cart_updated_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.users.user_name}'s Cart"