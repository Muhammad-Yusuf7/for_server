from .models import Api
from rest_framework import viewsets, permissions
from .serializers import ApiSerializer


# Todo ViewSet
class ApiViewSet(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ApiSerializer