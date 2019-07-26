from rest_framework import routers
from .viewsets import ProductoViewSets

router = routers.SimpleRouter()
router.register('producto', ProductoViewSets)

urlpatterns = router.urls