from django.urls import path
from . import views
from rest_framework import routers
from .api import ApiViewSet

router = routers.DefaultRouter()
router.register('api/arguments', ApiViewSet, 'arguments')
urlpatterns = [
    path('<int:link_id>/',views.index)
]

urlpatterns += router.urls
