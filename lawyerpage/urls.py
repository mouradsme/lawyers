from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fa', views.fa, name='fa'),
    path('loginA', views.loginA, name='loginA'),
    # other paths
]