from rest_framework import serializers

from department.serializers import DepartmentSerializer
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_name', 'first_name', 'email', 'photo', 'departament']


class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_name', 'first_name', 'email', 'photo', 'password', 'login', 'departament']


class UserListSerializer(serializers.ModelSerializer):
    departament = DepartmentSerializer(required=True)

    class Meta:
        model = User
        fields = ['id', 'photo', 'first_name', 'departament']


class UserListSerializerQP(serializers.Serializer):
    departament_id = serializers.IntegerField(allow_null=True, default=None)


class UserUploadPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['photo']
