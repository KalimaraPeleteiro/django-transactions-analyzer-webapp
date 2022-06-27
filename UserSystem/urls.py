from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('enter', views.enter, name='enter')
]
