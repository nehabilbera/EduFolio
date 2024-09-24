from django.urls import path

from . import views

    
urlpatterns = [
    path('',views.homePage),
    path('home/',views.homePage, name='home'),
    path('signin/', views.loginView, name='signin'),
    path('signup/', views.signupView, name="signup"),
    
    path('view/', views.viewPage, name='view'),
    path('search/', views.searchResources, name="search"),
    path('upload/', views.uploadPage, name="upload"),
    path('search_submit/', views.searchPage, name="search_submit"),
    path('resource_submit/', views.resourceSubmit, name="resource_submit"),

    
    path('login/', views.userLogin, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
]