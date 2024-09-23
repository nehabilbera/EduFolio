from django.urls import path

from . import views

    
urlpatterns = [
    path('',views.homePage),
    path('home/',views.homePage, name='home'),
    path('signin/', views.loginView, name='signin'),
    path('signup/', views.signupView, name="signup"),
    path('view/', views.viewPage, name='view'),
    path('upload/', views.uploadPage, name="upload"),
    
    path('login/', views.userLogin, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    
    path('resource_submit/', views.resourceSubmit, name="resource_submit"),
    
    path("dashboard/", views.dashboard, name="dashboard"),
]