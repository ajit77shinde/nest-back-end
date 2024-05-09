from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=255)
    user_phone_number = models.CharField(max_length=15)
    user_address = models.TextField()
    #extra field
    user_created_date = models.DateTimeField(auto_now_add=True,editable=False)
    user_updated_date = models.DateTimeField(auto_now = True)
    user_is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.user_name