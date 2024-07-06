from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('api/get_user_profile/', views.get_user_profile),
    path('get/', views.user_view, name='users')
]
