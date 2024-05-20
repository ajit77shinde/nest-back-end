from django.contrib import admin
from django.urls import path,include
#from api.urls import product_router, category_router
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.registry.extend(product_router.registry)
# router.registry.extend(category_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('product.urls')),
    # path('api/',include(router.urls)),
    path('api/',include('api.urls')),
    path('api/auth/', include('users.urls')),
]
