from django.shortcuts import render
from django.http import JsonResponse

def loginView(req):
    return render(req, 'logIn.html')
    
def signupView(req):
    return render(req, 'signUp.html')