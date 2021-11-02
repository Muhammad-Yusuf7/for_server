from rest_framework import routers
from .api import ApiViewSet

router = routers.DefaultRouter()
router.register('api/personal_num', ApiViewSet, 'personal_num')

urlpatterns = router.urls