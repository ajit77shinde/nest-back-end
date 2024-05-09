from django.urls import path, include
from . import views 
from rest_framework import routers
from . views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'product',ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('home', views.api_home, name='api_home'),
]