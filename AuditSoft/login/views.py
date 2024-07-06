from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# Create your views here.


def login_view(request):
    # Ваш код для обработки страницы входа
    return render(request, 'login/index.html')


@api_view(['GET'])
def get_user_profile(request):
    name = request.GET.get('name')
    password = request.GET.get('password')

    try:
        user = User.objects.get(name=name, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)


def user_view(request):
    # Ваш код для обработки страницы пользователей
    return render(request, 'login/users.html')
