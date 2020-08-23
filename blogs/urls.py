from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
    path('index/', views.IndexTemplateView.as_view(), name='index'),
    path('create/', views.CreateTemplateView.as_view(), name='create'),
]
