from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')



def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contactok')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

from mailjet_rest import Client
import os

def mailjettest(request):
    api_key = 'f6927cc5ef8f692e9ac4442b72018641'
    api_secret = '0e235092616214254b69917dd3b74d2f'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "wmaster468@gmail.com",
                    "Name": "Phinehas"
                },
                "To": [
                    {
                        "Email": "wmaster468@gmail.com",
                        "Name": "Phinehas"
                    }
                ],
                "Subject": "Greetings from Mailjet.",
                "TextPart": "My first Mailjet email",
                "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return render(request, 'login.html')
