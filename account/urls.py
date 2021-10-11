from django.urls import path
from account.views import *
from account.views import RegistrationView

urlpatterns = [
    path('', RegistrationView.as_view(),name='registration'),
    path('mail/',mail,name='mail'),  


]