from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django import forms
from .models import Mesa
import requests

# Create your views here.


class MesForm(forms.Form):
    sender = forms.EmailField(label='Enter your e-mail')
    message = forms.CharField(widget=forms.Textarea,
                              label='Your message',
                              min_length=4, max_length=250)


def mes(request):
    if request.user.is_authenticated:
        if request.user.is_staff is True:
            return HttpResponseRedirect('/admin/')
        else:
            if request.method == 'POST':
                form = MesForm(request.POST)
                if form.is_valid():
                    sender = form.cleaned_data['sender']
                    message = form.cleaned_data['message']
                    recipient = User.objects.filter(is_superuser=True)[0]
                    url = 'https://jsonplaceholder.typicode.com/users/?email='\
                        + sender
                    response = requests.get(url)
                    response = tuple(response)
                    response = str(response)
                    response = response.replace('(', '')
                    response = response.replace("b'", '')
                    response = response.replace('[', '')
                    response = response.replace('{', '')
                    response = response.replace("\\n", '')
                    response = response.replace("', ", '')
                    response = response.replace('}', '')
                    response = response.replace(']', '')
                    response = response.replace(')', '')
                    response = response.replace("'", '')
                    mesformesa = message
                    if len(response) > 2:
                        # im sorry about this
                        message = message + '\n \n Information about user from jsonplaceholder.typicode.com/users:\n' + response
                    recipient.email_user('Message from test1', message)
                    a_record = Mesa(sender=sender, message=mesformesa)
                    a_record.save()
                    return render(request, 'ok.html')
            else:
                form = MesForm()
            return render(request, 'message.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def lgt(request):
    logout(request)
    return HttpResponseRedirect('/login/')
