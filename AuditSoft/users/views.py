from django.shortcuts import render

# Create your views here.


def user_view(request):
    # Ваш код для обработки страницы входа
    return render(request, 'users/index.html')
