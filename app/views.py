from django.shortcuts import render
from django.http import JsonResponse

def loginView(req):
    return render(req, 'logIn.html')
    
def signupView(req):
    return render(req, 'signUp.html')

def homePage(req):
    return render(req, 'navbar.html')

def viewPage(req):
    return render(req, 'view.html')

def uploadPage(req):
    return render(req, 'upload.html')