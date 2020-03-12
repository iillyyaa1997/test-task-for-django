from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from auth2 import serializers


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = Token.objects.get_or_create(user=serializer.validated_data['user'])[0]
        return Response(data={'token': token.key}, status=status.HTTP_200_OK)
