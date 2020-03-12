from rest_framework import generics
from rest_framework.exceptions import ValidationError

from department.models import Department
from department.permissions import IsAdmin
from department.serializers import DepartmentSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAdmin,)
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdmin,)
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.departament == instance:
            raise ValidationError({'message': 'You cannot delete the department to which you belong'})

        return super().delete(request, args, kwargs)
