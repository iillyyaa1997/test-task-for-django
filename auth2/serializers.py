from rest_framework import serializers

from user.models import User


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=256)
    password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        login = attrs.get('login')
        password = attrs.get('password')
        try:
            user = User.objects.get(login=login, password=password)
        except User.DoesNotExist:
            raise serializers.ValidationError({'message': 'This user does not exist.'})

        attrs['user'] = user
        return attrs
