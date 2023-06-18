from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='app/home.html'), name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/register', views.Register.as_view(), name='register')
]
