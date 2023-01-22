from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'sender/home.html')



# array of emails to send the mails

def sender(request):
    send_mail(
        'Hello Binayak ',
        'Hello Binayak How do you do?',
        'sudipbhandari67@gmail.com',
        ['binayakpokhrel005@gmail.com'],
        fail_silently=False
    )
    return HttpResponse('ender page')

