from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated

from department.permissions import IsAdmin, IsAdminUser
from user.models import User
from user.serializers import UserSerializer, UserFullSerializer, UserListSerializer, UserListSerializerQP, \
    UserUploadPhotoSerializer


class UserCreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserFullSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserListSerializer
    serializer_query_params_class = UserListSerializerQP
    queryset = User.objects.all().order_by('-last_name')

    def get_queryset(self):
        if self.request.user.role == User.Role.USER:
            return self.request.user.departament.users.all()

        departament_id = self.request.query_params.get('departament_id')
        if departament_id:
            return self.queryset.filter(departament_id=int(departament_id))
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        serializer_qp = self.serializer_query_params_class(data=request.query_params)
        serializer_qp.is_valid(raise_exception=True)
        test = super().get(request, args, kwargs)
        return test


class UserUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAdmin,)
    serializer_class = UserFullSerializer
    queryset = User.objects.all()


class UserRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUploadPhotoView(generics.UpdateAPIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAdmin,)
    queryset = User.objects.all()
    serializer_class = UserUploadPhotoSerializer
