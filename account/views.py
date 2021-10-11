from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core.mail import send_mail   
from django.contrib.auth import authenticate, login

from myproject import settings  

from .models import Registration
 

# Create your views here.

class RegistrationView(View):
    def post(self, request):
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        registration = Registration(full_name=fullname, email=email, username=username, password=password)
        registration.save()
        mail(request)
        return HttpResponse("Your details register")        

    def get(self, request):
        return render(request, 'registration.html')
    
    
def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for you are successfully login"  
    to      = "nishachouhan232@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  




