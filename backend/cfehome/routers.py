from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register('product-bde', ProductViewSet, basename='products')
urlpatterns = router.urls