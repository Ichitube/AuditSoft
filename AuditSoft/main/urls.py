from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
]
