from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
# Create your views here.


class RegForm(forms.Form):
    name = forms.CharField(label='Enter your username',
                           min_length=4, max_length=14)
    psw1 = forms.CharField(widget=forms.PasswordInput,
                           label='Enter your password',
                           min_length=4, max_length=14)
    psw2 = forms.CharField(widget=forms.PasswordInput,
                           label='Repeat your password',
                           min_length=4, max_length=14)


def reg(request):
    if request.user.is_authenticated:
        if request.user.is_staff is True:
            return HttpResponseRedirect('/admin/')
        else:
            return HttpResponseRedirect('/message/')
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            p1 = form.cleaned_data['psw1']
            p2 = form.cleaned_data['psw2']
            if User.objects.filter(username=n).exists():
                context = 'Username is not avaliable. Try again'
            else:
                if p1 == p2:
                    user = User.objects.create_user(n, None, p1)
                    user.save()
                    return HttpResponseRedirect('/login/')
                else:
                    context = 'You have entered different passwords!'
            return render(request, 'err.html', {'context': context})
    else:
        form = RegForm()
    return render(request, 'reg.html', {'form': form})
