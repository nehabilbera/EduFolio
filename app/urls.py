from django.urls import path

from . import views

    
urlpatterns = [
    path('signin/', views.loginView, name='signin'),
    path('signup/', views.signupView, name="signup")
]