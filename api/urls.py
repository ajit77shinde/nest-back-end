from django.urls import path, include
from . import views 
from rest_framework import routers
from . views import ProductViewSet,CategoryViewSet

# product_router = routers.DefaultRouter()
# product_router.register(r'product',ProductViewSet)
# category_router = routers.DefaultRouter()
# category_router.register(r'category',CategoryViewSet)
router = routers.DefaultRouter()
router.register(r'category',CategoryViewSet)
router.register(r'product',ProductViewSet)


urlpatterns = [
    # path('', include(product_router.urls)),
    # path('', include(category_router.urls)),
    path('',include(router.urls)),
    path('home', views.api_home, name='api_home'),
]