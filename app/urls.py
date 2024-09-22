from django.urls import path

from . import views

    
urlpatterns = [
    path('',views.homePage),
    path('home/',views.homePage, name='home'),
    path('signin/', views.loginView, name='signin'),
    path('signup/', views.signupView, name="signup"),
    path('view/', views.viewPage, name='view'),
    path('upload/', views.uploadPage, name="upload"),
    
    path('resource_submit/', views.resourceSubmit, name="resource_submit"),
]