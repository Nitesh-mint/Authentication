from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView
urlpatterns = [
    path("home/", TemplateView.as_view(template_name='home.html'), name= 'home'),
    path("signup/", SignUpView.as_view(), name="signup"),
]