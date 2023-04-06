from rest_framework import viewsets

from applications.base.permission import IsAdminUser
from applications.base.response import operation_success
from applications.cert.models import University
from applications.cert.serializers import UniversitySerializer


# Create your views here.

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    # permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return operation_success
