from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from users.models import User
from users.serializers import SendConfirmationCodeSerializer, TokenSerializer


class SignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SendConfirmationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        username = serializer.validated_data['username']
        user, created = User.objects.get_or_create(
            email=email,
            username=username,
        )
        if not created:
            user.email = email
            user.username = username
            user.save()
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            'Код подтверждения API YamDB',
            (
                f'Имя пользователя {user.username}'
                '\n'
                f'Код подтверждения {confirmation_code}'
            ),
            f'{settings.EMAIL_FROM}',
            [f'{email}'],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User,
            username=serializer.validated_data['username'],
        )

        confirmation_code = request.data.get('confirmation_code')
        refresh = RefreshToken.for_user(user)

        if default_token_generator.check_token(user, confirmation_code):
            AccessToken.for_user(user)
            user.save()
            return Response(
                {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            )

        return Response(
            {'Error': 'Неверный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST,
        )
