from rest_framework import viewsets, permissions
from .serializers import ApiSerializer
from .models import Control

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ApiSerializer